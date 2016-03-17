import environment, sys, re, ast, random, ast, codegen, inspect, copy
from codegen import to_source

class MutantTransformer(ast.NodeTransformer):

    mutants_visited = environment.resources["seed"]
    
    def __init__(self, mutation='comment_single_line', strip_decorators = True):
        self.strip_decorators = strip_decorators
        self.mutation = mutation

    #NOTE: This will work differently depending on whether the decorator takes arguments. 
    def visit_FunctionDef(self, node):
        if environment.resources["mutating"]==False: return self.generic_visit(node)
        random.seed(environment.resources["seed"])
        node.name += '_mod'  #  so we don't overwrite Python's object caching
        if self.strip_decorators == True:
            node.decorator_list = []
        lines_to_check = node.body
        if self.mutation == 'comment_single_line':
            if len(lines_to_check) > 0: node.body.remove(random.choice(lines_to_check))
        elif self.mutation == 'truncate_function':
            truncation_point = random.randint(1,len(lines_to_check) - 1)
            for line in lines_to_check[truncation_point:]:
                node.body.remove(line)
        elif self.mutation == 'comment_line_chance_20':
            if random.randint(0,4) == 0:
                if len(lines_to_check) > 0: node.body.remove(random.choice(lines_to_check))
        MutantTransformer.mutants_visited += 1
        environment.resources["seed"] += 1
        return self.generic_visit(node)

def mutate__comment_single_line(func):
    def wrapper(*args, **kwargs):
        generic_retrieve_mutation((func), 'comment_single_line')(*args, **kwargs)
    return wrapper

def mutate__truncate_function(func):
    def wrapper(*args, **kwargs):
        generic_retrieve_mutation((func), 'truncate_function')(*args, **kwargs)
    return wrapper

def mutate__comment_line_chance_20(func):
    def wrapper(*args, **kwargs):
        generic_retrieve_mutation((func), 'comment_line_chance_20')(*args, **kwargs)
    return wrapper

def generic_retrieve_mutation(func, mutation_type):
    compiled_mutant = mutate_function((func), mutation_type)
    mutated_function = (func)
    mutated_function.func_code = compiled_mutant
    cache[(func, mutation_type)] = mutated_function
    return mutated_function

def mutate_function(function, mutation_type ="comment_single_line"):
    if function in cache.keys():
        function_source = cache[function]
    else:
        function_source = inspect.getsourcelines(function)[0]  # This is our problem: always gives us the first function.
        cache[function] = function_source
    function_source = ''.join(function_source) + '\n' + function.func_name + '_mod' + '()'
    mutator = MutantTransformer(mutation_type)
    abstract_syntax_tree = ast.parse(function_source)
    mutated_function = mutator.visit(abstract_syntax_tree)
    return compile(mutated_function, inspect.getsourcefile(function), 'exec')

def exec_wrapper(mutant):
    exec(mutant)

class ResourcesExpendedException(Exception):
    pass


cache = {}


def atom(func):
    def wrapper(*args, **kwargs):
        if precondition():
            #generic_retrieve_mutation(func, 'comment_single_line')(*args, **kwargs)
            func(*args, **kwargs)
#             post_function_sequence(**kwargs)
    
    return wrapper

def flow(func):
    def wrapper(*args, **kwargs):
        if precondition():
            func(*args, **kwargs)
    return wrapper

# to be run after every function, say, to decrease time in a budget.
def post_function_sequence(kwargs):
    for key, value in kwargs.iteritems():
        environment.resources[key] += value  # If we're only using integers?!
        print key, value

def system_setup(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)  # Run setup functions no matter what...
    return wrapper

def metric(func):
    def wrapper(*args, **kwargs):
        if metric_successful():
            func(*args, **kwargs)
    return wrapper

# A boolean function that tells you whether you should be running the function passed into the decorator or not. 
# This should be a bool for any implementation of the system. 
def precondition():
    result = environment.resources["time"] >= 0
    if not result: 
        raise ResourcesExpendedException()
    return result

def metric_successful():
    return environment.resources["time"] >= 0

class atom_args(object):
    def __init__(self, **kwargs):
        self.modifications = kwargs

    def __call__(self, func):
        def wrap(*args):
            if precondition():
                func(*args)
                post_function_sequence(self.modifications)
        return wrap


class Mutator(ast.NodeTransformer):

    mutants_visited = 0

    # The mutation argument is a function that takes a list of lines and returns another list of lines.
    def __init__(self, mutation=lambda x: x, strip_decorators = True):
        self.strip_decorators = strip_decorators
        self.mutation = mutation

    #NOTE: This will work differently depending on whether the decorator takes arguments.
    def visit_FunctionDef(self, node):
        # Only actually mutate if we have the necessary flags
        if environment.resources["mutating"]==False: return self.generic_visit(node)

        # Fix the randomisation to the environment
        random.seed(environment.resources["seed"])

        # Mutation algorithm!
        node.name += '_mod'   # so we don't overwrite Python's object caching
        # Remove decorators if we need to So we don't re-decorate when we run the mutated function, mutating recursively
        if self.strip_decorators:
            node.decorator_list = []
        # Mutate! self.mutation is a function that takes a list of line objects and returns a list of line objects.
        node.body = self.mutation(node.body)

        # Now that we've mutated, increment the necessary counters and parse the rest of the tree we're given
        Mutator.mutants_visited += 1
        environment.resources["seed"] += 1
        return self.generic_visit(node)


class mutate(object):
    def __init__(self, mutation_type):
        self.mutation_type = mutation_type

    def __call__(self, func):
        def wrap(*args, **kwargs):

            # Load function source from cache if available
            if func in cache.keys():
                func_source = cache[func]
            else:
                func_source = inspect.getsourcelines(func)[0]  # This is our problem: always gives us the first func.
                cache[func] = func_source
            # Create function source
            func_source = ''.join(func_source) + '\n' + func.func_name + '_mod' + '()'
            # Mutate using the new mutator class
            mutator = Mutator(self.mutation_type)
            abstract_syntax_tree = ast.parse(func_source)
            mutated_func_uncompiled = mutator.visit(abstract_syntax_tree)
            mutated_func = func
            mutated_func.func_code = compile(mutated_func_uncompiled, inspect.getsourcefile(func), 'exec')
            cache[(func, self.mutation_type)] = mutated_func
            mutated_func(*args, **kwargs)
        return wrap


# This is simply to indicate to our mutation library that this atom needs a line commented.
def mutate_comment_line(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper


# This is simply to indicate to our mutation library that this atom should have its contents ignored.
def mutate_ignore(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper

