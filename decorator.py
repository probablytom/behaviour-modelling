from resources import resources

def atom(func):
    def wrapper(*args, **kwargs):
        if precondition():
            print "Running function"
            func(*args, **kwargs)
            post_function_sequence(*args, **kwargs)
    
    return wrapper

# to be run after every function, say, to decrease money in a budget.
def post_function_sequence(**kwargs):
    for key, value in kwargs.itervalue():
        resources[key] += value  # If we're only using integers?!

# A boolean function that tells you whether you should be running the function passed into the decorator or not. 
# This should be a bool for any implementation of the system. 
def precondition():
    return resources["money"] >= 0
