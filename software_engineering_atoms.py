import random
from logger import Logger
from environment import resources


# For keeping a log / printing to the console
# filepath-----\/           Logging--\/   printing--\/
log = Logger(   "event.log",         True,           False)


# -----------------------------------------------------------------------------
# HELPER FUNCTIONS
# -----------------------------------------------------------------------------

# bool(random.getrandbits(1)) if we want to be fast!
def random_boolean():
    return random.choice([True, False])


# -----------------------------------------------------------------------------
# LOW LEVEL ACTIONS
# atomic activity for actual activity within the sociotechnical system
# all interactions with resources, shouldn't be anything else...
# -----------------------------------------------------------------------------

def run_model():
    create_branch()

# The functions that act as actions within the flowchart
def create_branch():
    log.log_line("Creating new branch")
    resources["branches"] += 1

def create_ticket():
    resources["tickets"] += 1

def checkout_branch():
    pass

def write_tests():
    log.log_line("Writing tests")
    resources['money'] -= 100
    resources["stress"] += 0.1

def write_code():
    log.log_line("Writing code")
    resources["money"] -= 100
    resources["stress"] += 0.05

def run_tests():
    log.log_line("Running tests against code")
    resources["tests passing"] = random_boolean()  
    resources["money"] -= 100
    if resources["tests passing"]:
        log.log_line("\t- Tests successful!")
        resources["stress"] -= 0.1
    else:
        log.log_line("\t- Tests unsuccessful")
        log.log_line("\t- Rewriting tests")
        resources["stress"] += 0.1

def integration_test():
    log.log_line("Running integration test")
    resources["money"] -= 100
    resources["integration tests passing"] = random_boolean()

def determine_whether_integration_tests_running():
    if resources["integration tests passing"]:
        log.log_line("\t- Integration test successful!")
        resources["stress"] -= 0.05
        resources["integration tests passing"] = True
    else:
        log.log_line("\t- Integration test unsuccessful")
        log.log_line("\t- Rewriting tests")
        resources["stress"] += 0.05
        resources["integration tests passing"] = False

def merge():
    log.log_line("Merging branch against codebase")
    resources["branches"] -= 1
    resources["money"] -= 100
    resources["stress"] += 0.05  # Because merging is always stressful, particularly with a large codebase. 
    # Perhaps this should scale to some "changes made" resource that gets incremented by the code and test writing?

def user_acceptance_test():
    log.log_line("Performing user acceptance tests")
    resources["money"] -= 100
    resources["user acceptance tests passing"] = random_boolean()
    if resources["user acceptance tests passing"]:
        log.log_line("\t- Test successful!")
        resources["stress"] -= 0.05
    else:
        log.log_line("\t- Test unsuccessful")
        log.log_line("\t- Rewriting tests")
        resources["stress"] += 0.05

def attempt_deployment():
    log.log_line("Deploying product")
    resources["stress"] += 0.1
    resources["money"] -= 100
    resources["successful deployment"] = random_boolean()
    if resources["successful deployment"]:
        log.log_line("\t- Deployment successful!")
        resources["tickets"] -= 1
    else:
        log.log_line("\t- Problems with building")
        log.log_line("\t- Rerunning integration test")

def gather_statistics_and_log():
    log.log_line("--------------------------------------------------------------------------------")
    log.log_line("Complete!")
    log.log_line()

    for key in resources.keys():
        log.log_line(key + ":\t\t" + str(resources[key]))
    log.log_line("--------------------------------------------------------------------------------")

