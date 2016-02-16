import base, environment

def atom(func):
    def wrapper(*args, **kwargs):
        if precondition():
            #base.generic_retrieve_mutation(func, 'comment_single_line')(*args, **kwargs)
            func(*args, **kwargs)
#             post_function_sequence(**kwargs)
    
    return wrapper

def flow(func):
    def wrapper(*args, **kwargs):
        if precondition():
            func(*args, **kwargs)
    return wrapper

# to be run after every function, say, to decrease money in a budget.
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
    result = environment.resources["money"] >= 0
    if not result: 
        raise base.ResourcesExpendedException()
    return result

def metric_successful():
    return environment.resources["money"] >= 0

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

