import random
from logger import Logger

# Resources regarding the workflow's environment
time = 0 # to be incremented upon every step


# The resources we'll be editing
# NOTE: These should ordinarily be amended to reflect the project...
resources = {}
resources["stress"] = 0.1
resources["building"] = True
resources["money"] = 10000
log = Logger("event.log", True, False)

# -----------------------------------------------------------------------------


def random_boolean():
    return random.choice([True, False])


# -----------------------------------------------------------------------------


def run_model():
    create_branch()

# The functions that act as actions within the flowchart
def create_branch():
    log.log_line("Creating new branch")
    # write_tests()

def write_tests():
    log.log_line("Writing tests")
    resources['money'] -= 100
    resources["stress"] += 0.1
    # write_code()

def write_code():
    log.log_line("Writing code")
    resources["money"] -= 100
    resources["stress"] += 0.05
    # run_tests()

def run_tests():
    log.log_line("Running tests against code")
    resources["building"] = random_boolean()  
    resources["money"] -= 100
    if resources["building"]:
        log.log_line("\t- Tests successful!")
        resources["stress"] -= 0.1
        # integration_test()
    else:
        log.log_line("\t- Tests unsuccessful")
        log.log_line("\t- Rewriting tests")
        resources["stress"] += 0.1
        # write_tests()

def integration_test():
    log.log_line("Running integration test")
    resources["money"] -= 100
    resources["building"] = random_boolean()  
    if resources["building"]:
        log.log_line("\t- Integration test successful!")
        resources["stress"] -= 0.05
        # merge()
    else:
        log.log_line("\t- Integration test unsuccessful")
        log.log_line("\t- Rewriting tests")
        resources["stress"] += 0.05
        # write_tests()

def merge():
    log.log_line("Merging branch against codebase")
    resources["money"] -= 100
    resources["stress"] += 0.05  # Because merging is always stressful, particularly with a large codebase. 
    # Perhaps this should scale to some "changes made" resource that gets incremented by the code and test writing?
    # user_acceptance_test()

def user_acceptance_test():
    log.log_line("Performing user acceptance tests")
    resources["money"] -= 100
    resources["building"] = random_boolean()  
    if resources["building"]:
        log.log_line("\t- Test successful!")
        resources["stress"] -= 0.05
        # deploy()
    else:
        log.log_line("\t- Test unsuccessful")
        log.log_line("\t- Rewriting tests")
        resources["stress"] += 0.05
        # write_tests()

def deploy():
    log.log_line("Deploying product")
    resources["stress"] += 0.1
    resources["money"] -= 100
    if not resources["building"]:
        log.log_line("\t- Problems with building")
        log.log_line("\t- Rerunning integration test")
        integration_test()
    else:
        log.log_line("\t- Deployment successful!")
        # complete()

def complete():
    print
    print "Complete!"
    log.log_line("--------------------------------------------------------------------------------")
    log.log_line("Complete!")

    for key in resources.keys():
        log.log_line(key + ":\t\t" + str(resources[key]))
    print "--------------------------------------------------------------------------------"


# -----------------------------------------------------------------------------
# run_model()
