from environment import resources

def atom(func):
    def wrapper(*args, **kwargs):
        if precondition():
            print "Running decorator"
            func(*args, **kwargs)
            post_function_sequence(**kwargs)
    
    return wrapper

# to be run after every function, say, to decrease money in a budget.
def post_function_sequence(kwargs):
    print "post_func"
    for key, value in kwargs.iteritems():
        resources[key] += value  # If we're only using integers?!
        print key, value

# A boolean function that tells you whether you should be running the function passed into the decorator or not. 
# This should be a bool for any implementation of the system. 
def precondition():
    return resources["money"] >= 0



class atom_args(object):
    def __init__(self, **kwargs):
        self.modifications = kwargs

    def __call__(self, func):
        def wrap(*args):

            if precondition():
                func(*args)
                post_function_sequence(self.modifications)
        return wrap
