import random
from logger import Logger
from Register import Registrar


# The resources we'll be editing
# NOTE: These should ordinarily be amended to reflect the project...
resources = {}
resources["stress"] = 0.1
resources["building"] = True
resources["money"] = 10000
resources["tests passing"] = False
resources["integration tests passing"] = False
resources["user acceptance tests passing"] = False
resources["successful deployment"] = False

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
        resources["tests passing"] = True
    else:
        log.log_line("\t- Tests unsuccessful")
        log.log_line("\t- Rewriting tests")
        resources["stress"] += 0.1
        resources["tests passing"] = False

def integration_test():
    log.log_line("Running integration test")
    resources["money"] -= 100
    resources["building"] = random_boolean()  
    if resources["building"]:
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
    resources["money"] -= 100
    resources["stress"] += 0.05  # Because merging is always stressful, particularly with a large codebase. 
    # Perhaps this should scale to some "changes made" resource that gets incremented by the code and test writing?

def user_acceptance_test():
    log.log_line("Performing user acceptance tests")
    resources["money"] -= 100
    resources["building"] = random_boolean()  
    if resources["building"]:
        log.log_line("\t- Test successful!")
        resources["stress"] -= 0.05
        resources["user acceptance tests passing"] = True
    else:
        log.log_line("\t- Test unsuccessful")
        log.log_line("\t- Rewriting tests")
        resources["stress"] += 0.05
        resources["user acceptance tests passing"] = False

def deploy():
    log.log_line("Deploying product")
    resources["stress"] += 0.1
    resources["money"] -= 100
    if resources["building"]:
        log.log_line("\t- Deployment successful!")
        resources["successful deployment"] = True
    else:
        log.log_line("\t- Problems with building")
        log.log_line("\t- Rerunning integration test")
        resources["successful deployment"] = False

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

def implement_feature():
    write_tests()
    write_code()
    run_tests()

def feature_integration():
    integration_test()

def user_acceptance_testing():
    user_acceptance_test()

def attempt_deployment():
    deploy()


def print_statistics():
    complete()


# -----------------------------------------------------------------------------
# CONTROL ARCHITECTURE
# dynamic control flow
# making decisions based on outcomes of events
# not just chaining together actions, now we're creating the actual model
# -----------------------------------------------------------------------------


def begin_feature_implementation():
    implement_feature()
    while not resources["tests passing"]:
        implement_feature()

def integrate_feature_into_codebase():
    feature_integration()
    while not resources["integration tests passing"]:
        feature_integration()
    merge()  # Should this be here or separate?

def run_user_acceptance_tests():
    user_acceptance_testing()
    while not resources["user acceptance tests passing"]:
        user_acceptance_testing()

def begin_deployment_of_feature():
    attempt_deployment()
    while not resources["successful deployment"]:
        # here there *should* be a link back to the integrate_feature loop. How do we do this with our current model?
        pass  # TO COMPLETE TO COMPLETE TO COMPLETE TO COMPLETE TO COMPLETE TO COMPLETE TO COMPLETE TO COMPLETE

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
# REGISTER
# turn the functions we're defining here into a saved, callable model
# -----------------------------------------------------------------------------


registrar = Registrar()
registrar.register("Began feature implementation", begin_feature_implementation)
registrar.register("Integrated feature into codebase", integrate_feature_into_codebase)
registrar.register("Ran user acceptance test", run_user_acceptance_tests)
registrar.register("Began deployment of feature", begin_deployment_of_feature)
registrar.commit()

# -----------------------------------------------------------------------------
# RUN
# begin the model!
# -----------------------------------------------------------------------------

#begin()
