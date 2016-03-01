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
    compiled_mutant = mutate((func), mutation_type)
    mutated_function = (func)
    mutated_function.func_code = compiled_mutant
    cache[(func, mutation_type)] = mutated_function
    return mutated_function

def mutate(function, mutation_type = "comment_single_line"):
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

