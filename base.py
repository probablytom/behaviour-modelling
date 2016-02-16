import sys, re, ast, random, ast, codegen, inspect, base, copy, environment
from codegen import to_source

class MutantTransformer(ast.NodeTransformer):

    mutants_visited = environment.resources["seed"]
    
    def __init__(self, mutation='comment_single_line', strip_decorators = True):
        self.strip_decorators = strip_decorators
        self.mutation = mutation

    #NOTE: This will work differently depending on whether the decorator takes arguments. 
    def visit_FunctionDef(self, node):
        random.seed(MutantTransformer.mutants_visited)
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
