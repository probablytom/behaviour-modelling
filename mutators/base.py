import sys, re, ast, random, ast, codegen, inspect, base, copy
from codegen import to_source

class MutantTransformer(ast.NodeTransformer):

    def __init__(self, mutation='comment_single_line', strip_decorators = True):
        self.source_lines = source_lines
        self.strip_decorators = strip_decorators
        self.mutation = mutation

    #NOTE: This will work differently depending on whether the decorator takes arguments. 
    def visit_FunctionDef(self, node):
        if self.strip_decorators == True:
            node.decorator_list = []
        lines_to_check = node.body
        if self.mutation == 'comment_single_line':
            if len(lines_to_check) > 0: node.body.remove(random.choice(lines_to_check))
        elif self.mutation == 'truncate_function':
            truncation_point = random.randint(0,len(lines_to_check) - 1)
            node.body = node.body[truncation_point:]
        return self.generic_visit(node)

def mutate__comment_single_line(func):
    source_to_run = ""
    def wrapper(*args, **kwargs):
        to_run = generic_retrieve_mutation(func, 'comment_single_line')
        to_run(*args, **kwargs)
    return wrapper

def mutate__truncate_function(func):
    source_to_run = ""
    def wrapper(*args, **kwargs):
        generic_retrieve_mutation(func, 'truncate_function')(*args, **kwargs)
        print cache
    return wrapper

def generic_retrieve_mutation(func, mutation_type):
    # Commented so we don't really cache
    # if (func, mutation_type) in cache.keys(): 
    #    return cache[(func, mutation_type)]
    compiled_mutant = mutate(func, mutation_type)
    mutated_function = copy.copy(func)
    mutated_function.func_code = compiled_mutant
    cache[func] = mutated_function
    return mutated_function

def mutate(function, mutation_type = "comment_single_line"):
    function_source = inspect.getsourcelines(function)[0]
    function_source = ''.join(function_source) + '\n' + function.func_name + '()'
    mutator = MutantTransformer(function_source, mutation_type)
    abstract_syntax_tree = ast.parse(function_source)
    mutated_function = mutator.visit(abstract_syntax_tree)
    return compile(mutated_function, '<ast>', 'exec')

def exec_wrapper(mutant):
    exec(mutant)

# random.seed("mutation testing")
cache = {}
