from random import random as random_float

# Resources regarding the workflow's environment
time = 0 # to be incremented upon every step


# The resources we'll be editing
# NOTE: These should ordinarily be amended to reflect the project...
resources = {}
resources["stress"] = 0.1
resources["building"] = True
resources["money"] = 10000


# -----------------------------------------------------------------------------


def random_boolean():
    return random_float() > 0.5


# -----------------------------------------------------------------------------


def run_model():
    create_branch()

# The functions that act as actions within the flowchart
def create_branch():
    print "Creating branch"
    write_tests()

def write_tests():
    print "Writing tests"
    resources['money'] -= 100
    resources["stress"] += 0.1
    write_code()

def write_code():
    print "Writing code"
    resources["money"] -= 100
    resources["stress"] += 0.05
    run_tests()

def run_tests():
    print "Running tests against code"
    resources["building"] = random_boolean()  
    resources["money"] -= 100
    if resources["building"]:
        print "\t- Tests successful!"
        resources["stress"] -= 0.1
        integration_test()
    else:
        print "\t- Tests unsuccessful"
        print "\t- Rewriting tests"
        resources["stress"] += 0.1
        write_tests()

def integration_test():
    print "Running integration test"
    resources["money"] -= 100
    resources["building"] = random_boolean()  
    if resources["building"]:
        print "\t- Integration test successful!"
        resources["stress"] -= 0.05
        merge()
    else:
        print "\t- Integration test unsuccessful"
        print "\t- Rewriting tests"
        resources["stress"] += 0.05
        write_tests()

def merge():
    print "Merging branch against codebase"
    resources["money"] -= 100
    resources["stress"] += 0.05  # Because merging is always stressful, particularly with a large codebase. 
    # Perhaps this should scale to some "changes made" resource that gets incremented by the code and test writing?
    user_acceptance_test()

def user_acceptance_test():
    print "Performing user acceptance tests"
    resources["money"] -= 100
    resources["building"] = random_boolean()  
    if resources["building"]:
        print "\t- Test sucessful!"
        resources["stress"] -= 0.05
        deploy()
    else:
        print "\t- Test unsuccessful"
        print "\t- Rewriting tests"
        resources["stress"] += 0.05
        write_tests()

def deploy():
    print "Deploying!"
    resources["stress"] += 0.1
    resources["money"] -= 100
    if not resources["building"]:
        print "\t- Problems with building"
        print "\t- Rerunning integration test"
        integration_test()
    else:
        print "\t- Deployment successful!"
        complete()

def complete():
    print "--------------------------------------------------------------------------------"
    print "Complete!"

    for key in resources.keys():
        print key + ":\t\t" + str(resources[key])
    print "--------------------------------------------------------------------------------"


# -----------------------------------------------------------------------------
run_model()
