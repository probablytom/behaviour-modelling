import ast, codegen, inspect, base
def mutate__comment_single_line(func):
    source_to_run = ""
    def wrapper(*args, **kwargs):
        original_source =inspect.getsourcelines(func)[0] 
        func_source = ''.join(original_source) + '\n' + func.func_name + '()'
        t = ast.parse(func_source)
        mutator = base.MutantTransformer(func_source, 'comment_line')
        mutated_func = mutator.visit(t)
        compiled_mutant = compile(mutated_func, '<ast>', 'exec')
        exec_wrapper(compiled_mutant)
        #func.func_code = compiled_mutant
        #func(*args, **kwargs)
    return wrapper

def mutate__truncate_function(func):
    source_to_run = ""
    def wrapper(*args, **kwargs):
        original_source =inspect.getsourcelines(func)[0] 
        func_source = ''.join(original_source) + '\n' + func.func_name + '()'
        t = ast.parse(func_source)
        mutator = base.MutantTransformer(func_source, 'truncate_function')
        mutated_func = mutator.visit(t)
        compiled_mutant = compile(mutated_func, '<ast>', 'exec')
        exec_wrapper(compiled_mutant)
        #func.func_code = compiled_mutant
        #func(*args, **kwargs)
    return wrapper

def exec_wrapper(mutant):
    exec(mutant)

@mutate__comment_single_line
def test_comment():
    print 1 
    print 2 
    print 3  
    print 4
    print 5

@mutate__truncate_function
def test_truncate():
    print "the"
    print "quick"
    print "brown"
    print "fox"
    print "jumps"
    print "over"
    print "the"
    print "lazy"
    print "mutation"

test_comment()
print
test_truncate()
