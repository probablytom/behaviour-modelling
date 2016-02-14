import random
from logger import Logger
from environment import resources
from decorators import atom, atom_args  # Will need renaming



# For keeping a log / printing to the console
# filepath-----\/           Logging--\/   printing--\/
log = Logger(   "event.log",         False,           False)


# -----------------------------------------------------------------------------
# HELPER FUNCTIONS
# -----------------------------------------------------------------------------

# bool(random.getrandbits(1)) if we want to be fast!
def random_boolean():
    return random.choice([True, False])

# Note: this is specifically for detecting a hidden bug! I think this is all we need for bug-detection-probability-things
def probability_of_bug_being_detected():
    probability_of_not_detecting = 1 - resources["probability of bug being detected"]
    no_of_hidden_bugs = resources["number of hidden bugs"]
    return 1 - probability_of_not_detecting**no_of_hidden_bugs


# We write up to 20 lines of code, or remove up to 10
def estimate_lines_written():
    lower_bound = 0 if resources["lines of code"] < 10 else -10
    return random.choice([lower_bound, 20])

# Finding out how many bugs are in a collection of fresh lines of code
def number_of_new_bugs_in_lines(number_of_lines):
    return number_of_lines / 15


# -----------------------------------------------------------------------------
# LOW LEVEL ACTIONS
# atomic activity for actual activity within the sociotechnical system
# all interactions with resources, shouldn't be anything else...
# -----------------------------------------------------------------------------

@atom
def run_model():
    create_branch()

@atom
# The functions that act as actions within the flowchart
def create_branch():
    log.log_line("Creating new branch")
    resources["branches"] += 1

@atom
def create_ticket():
    resources["tickets"] += 1

@atom
def checkout_branch():
    pass

@atom
def begin_to_squash_bug():
    pass

@atom
def write_code_to_fix_bug():
    log.log_line("Writing code to fix bugs")
    resources["money"] -= 50
    resources["stress"] += 0.05
    number_of_new_lines_of_code = estimate_lines_written() / 2
    resources["lines of code"] += number_of_new_lines_of_code
    
    # Not increasing the number of hidden bugs as any bugs in the code being worked on should be picked up by the tests that are currently failing - is this correct?
    # Update: This is incorrect, as hidden bugs should be introduced, then discovered. Leaving it like this to fix later.
    # resources["number of hidden bugs"] += number_of_bugs_in_lines(number_of_new_lines_of_code)

@atom
def run_tests_on_bug():
    log.log_line("running tests on previously hidden bug to fix")
    resources["tests to squash bug passing"] = True if probability_of_bug_being_detected > 0.1 else False
    if resources["tests to squash bug passing"]:
        resources["number of bugs this iteration"] -= 1
        resources["number of bugs"] -= 1
        resources["number of failing tests this iteration"] -= 1
    else:
        pass
    resources["tests passing"] = (resources["number of failing tests this iteration"] == 0)

#@atom_args(money=-100, stress=0.1)
@atom
def write_tests():
    log.log_line("Writing tests")
    resources["number of tests"] += 1

@atom
def write_code():
    log.log_line("Writing code")
    resources["money"] -= 100
    resources["stress"] += 0.05
    number_of_new_lines_of_code = estimate_lines_written()
    number_of_bugs_added = number_of_new_bugs_in_lines(number_of_new_lines_of_code)
    resources["lines of code"] += number_of_new_lines_of_code
    resources["number of hidden bugs"] += number_of_bugs_added
    resources["number of bugs"] += number_of_bugs_added
    resources["number of bugs added this iteration"] += number_of_bugs_added
    
def run_tests():
    log.log_line("Running tests against code")
    for test in range(0, resources["number of tests"]):
        resources["current test passing"] = True if probability_of_bug_being_detected() > 0.15 else False
        resources["money"] -= 100
        if resources["current test passing"]:
            log.log_line("\t- Tests successful!")
            resources["stress"] -= 0.1
        else:
            log.log_line("\t- Tests unsuccessful")
            log.log_line("\t- Rewriting tests")
            resources["stress"] += 0.05
            resources["number of failing tests this iteration"] += 1
    resources["tests passing"] = (resources["number of failing tests this iteration"] == 0)

@atom
def integration_test():
    log.log_line("Running integration test")
    resources["money"] -= 100
    resources["integration tests passing"] = random_boolean()

@atom
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

@atom
def merge():
    log.log_line("Merging branch against codebase")
    resources["branches"] -= 1
    resources["money"] -= 100
    resources["stress"] += 0.05  # Because merging is always stressful, particularly with a large codebase. 
    # Perhaps this should scale to some "changes made" resource that gets incremented by the code and test writing?

@atom
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

@atom
def attempt_deployment():
    log.log_line("Deploying product")
    resources["stress"] += 0.1
    resources["money"] -= 100
    resources["successful deployment"] = random_boolean()
    if resources["successful deployment"]:
        log.log_line("\t- Deployment successful!")
        resources["tickets"] -= 1
        resources["stress"] -= -0.1
    else:
        log.log_line("\t- Problems with building")
        log.log_line("\t- Rerunning integration test")

@atom
def gather_statistics_and_log():
    log.log_line("--------------------------------------------------------------------------------")
    log.log_line("Complete!")
    log.log_line()

    for key in resources.keys():
        log.log_line(key + ":\t\t" + str(resources[key]))
    log.log_line("--------------------------------------------------------------------------------")

