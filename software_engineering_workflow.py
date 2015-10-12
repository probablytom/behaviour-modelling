import random
from logger import Logger


# The resources we'll be editing
# NOTE: These should ordinarily be amended to reflect the project...
resources = {}
resources["stress"] = 0.1
resources["building"] = True
resources["money"] = 10000

# For keeping a log / printing to the console
log = Logger("event.log", True, True)


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
    resources["building"] = random_boolean()  
    resources["money"] -= 100
    if resources["building"]:
        log.log_line("\t- Tests successful!")
        resources["stress"] -= 0.1
        return True
    else:
        log.log_line("\t- Tests unsuccessful")
        log.log_line("\t- Rewriting tests")
        resources["stress"] += 0.1
        return False

def integration_test():
    log.log_line("Running integration test")
    resources["money"] -= 100
    resources["building"] = random_boolean()  
    if resources["building"]:
        log.log_line("\t- Integration test successful!")
        resources["stress"] -= 0.05
        return True
    else:
        log.log_line("\t- Integration test unsuccessful")
        log.log_line("\t- Rewriting tests")
        resources["stress"] += 0.05
        return False

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
        return True
    else:
        log.log_line("\t- Test unsuccessful")
        log.log_line("\t- Rewriting tests")
        resources["stress"] += 0.05
        return False

def deploy():
    log.log_line("Deploying product")
    resources["stress"] += 0.1
    resources["money"] -= 100
    if resources["building"]:
        log.log_line("\t- Deployment successful!")
        return True
    else:
        log.log_line("\t- Problems with building")
        log.log_line("\t- Rerunning integration test")
        return False

def complete():
    log.log_line("--------------------------------------------------------------------------------")
    log.log_line("Complete!")
    log.log_line()

    for key in resources.keys():
        log.log_line(key + ":\t\t" + str(resources[key]))
    log.log_line("--------------------------------------------------------------------------------")


# -----------------------------------------------------------------------------
# HIGHER LEVEL ACTIONS
# chaining together the atomic actions
# static control flow, no dynamic flow yet
# -----------------------------------------------------------------------------

def implement_feature_outcome():
    write_tests()
    write_code()
    if run_tests(): return True
    else:           return False

def feature_integration_outcome():
    if integration_test():
        merge()
        return True
    else:
        return False

def user_acceptance_testing_outcome():
    return user_acceptance_test()

def attempt_deployment_outcome():
    return deploy


def print_statistics():
    complete()


# -----------------------------------------------------------------------------
# CONTROL ARCHITECTURE
# dynamic control flow
# making decisions based on outcomes of events
# not just chaining together actions, now we're creating the actual model
# -----------------------------------------------------------------------------

def begin_feature_implementation():
    if implement_feature_outcome(): integrate_feature_into_codebase()
    else: begin_feature_implementation()

def integrate_feature_into_codebase():
    if feature_integration_outcome(): run_user_acceptance_tests()
    else: begin_feature_implementation()

def run_user_acceptance_tests():
    if user_acceptance_testing_outcome(): begin_deployment_of_feature()
    else: begin_feature_implementation()

def begin_deployment_of_feature():
    if attempt_deployment_outcome(): end()
    else: integrate_feature_into_codebase()

def complete_activity():
    print_statistics()


# -----------------------------------------------------------------------------
# ACTION FUNCTIONS
# to kick everything off and bring it all to a halt
# -----------------------------------------------------------------------------

def begin():
    begin_feature_implementation()

def end():
    complete_activity()



# -----------------------------------------------------------------------------
# RUN
# begin the model!
# -----------------------------------------------------------------------------

begin()