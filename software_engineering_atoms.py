import random, environment
from logger import Logger
from decorators import atom, atom_args  # Will need renaming

# For keeping a log / printing to the console
# filepath-----\/           Logging--\/   printing--\/
log = Logger(   "event.log",         False,           False)

# -----------------------------------------------------------------------------
# HELPER FUNCTIONS
# -----------------------------------------------------------------------------

# Random boolean that returns False once out of every 10 times
def random_boolean():
    return random.choice(range(1, 11)) != 10


# Note: this is specifically for detecting a hidden bug! I think this is all we need for bug-detection-probability-things
def probability_of_bug_being_detected():
    return environment.resources["probability of bug being detected"]()


# We write up to 20 lines of code, or remove up to 10
def estimate_lines_written():
    lower_bound = 0 if environment.resources["lines of code"] < 10 else -10
    return random.choice([lower_bound, 20])

# Finding out how many bugs are in a collection of fresh lines of code
def number_of_new_bugs_in_lines(number_of_lines):
    return number_of_lines / 15


# -----------------------------------------------------------------------------
# LOW LEVEL ACTIONS
# atomic activity for actual activity within the sociotechnical system
# all interactions with environment.resources, shouldn't be anything else...
# -----------------------------------------------------------------------------

@atom
def run_model():
    create_branch()

@atom
# The functions that act as actions within the flowchart
def create_branch():
    log.log_line("Creating new branch")
    environment.resources["branches"] += 1

@atom
def create_ticket():
    environment.resources["tickets"] += 1

@atom
def checkout_branch():
    pass

@atom
def begin_to_squash_bug():
    pass

@atom
def write_code_to_fix_bug():
    log.log_line("Writing code to fix bugs")
    environment.resources["time"] -= 1
    environment.resources["stress"] += 0.05
    number_of_new_lines_of_code = estimate_lines_written() / 2
    environment.resources["lines of code"] += number_of_new_lines_of_code

@atom
def run_tests_on_bug():
    log.log_line("running tests on previously hidden bug to fix")
    environment.resources["tests to squash bug passing"] = True if probability_of_bug_being_detected > 0.5 else False
    if environment.resources["tests to squash bug passing"]:
        environment.resources["number of bugs this iteration"] -= 1
        environment.resources["number of bugs"] -= 1
        environment.resources["number of failing tests this iteration"] -= 1
    environment.resources["tests passing"] = (environment.resources["number of failing tests this iteration"] == 0)

#@atom_args(time=-3, stress=0.1)
@atom
def write_tests():
    log.log_line("Writing tests")
    environment.resources["number of tests"] += 1

@atom
def write_code():
    log.log_line("Writing code")
    environment.resources["time"] -= 2
    environment.resources["stress"] += 0.05
    number_of_new_lines_of_code = estimate_lines_written()
    number_of_bugs_added = number_of_new_bugs_in_lines(number_of_new_lines_of_code)
    environment.resources["lines of code"] += number_of_new_lines_of_code
    environment.resources["number of hidden bugs"] += number_of_bugs_added
    environment.resources["number of bugs"] += number_of_bugs_added
    environment.resources["number of bugs added this iteration"] += number_of_bugs_added
    
def run_tests():
    log.log_line("Running tests against code")
    for bug in range(0, environment.resources["number of failing tests this iteration"]):
        environment.resources["current test passing"] = True if probability_of_bug_being_detected() > 0.15 else False
        environment.resources["time"] -= 0
        if environment.resources["current test passing"]:
            log.log_line("\t- Tests successful!")
            environment.resources["stress"] -= 0.1
            environment.resources["number of failing tests this iteration"] -= 1
        else:
            log.log_line("\t- Tests unsuccessful")
            log.log_line("\t- Rewriting tests")
            environment.resources["stress"] += 0.05
            environment.resources["number of failing tests this iteration"] += 1
    environment.resources["tests passing"] = (environment.resources["number of failing tests this iteration"] == 0)

@atom
def integration_test():
    log.log_line("Running integration test")
    environment.resources["time"] -= 2
    environment.resources["integration tests passing"] = random_boolean()

@atom
def determine_whether_integration_tests_running():
    if environment.resources["integration tests passing"]:
        log.log_line("\t- Integration test successful!")
        environment.resources["stress"] -= 0.05
        environment.resources["integration tests passing"] = True
    else:
        log.log_line("\t- Integration test unsuccessful")
        log.log_line("\t- Rewriting tests")
        environment.resources["stress"] += 0.05
        environment.resources["integration tests passing"] = False

@atom
def merge():
    log.log_line("Merging branch against codebase")
    environment.resources["branches"] -= 1
    environment.resources["time"] -= 3
    environment.resources["stress"] += 0.05  # Because merging is always stressful, particularly with a large codebase. 
    # Perhaps this should scale to some "changes made" resource that gets incremented by the code and test writing?

@atom
def user_acceptance_test():
    log.log_line("Performing user acceptance tests")
    print "UA test"
    environment.resources["time"] -= 3
    environment.resources["user acceptance tests passing"] = random_boolean()
    print "user acceptance tests came out ", environment.resources["user acceptance tests passing"]
    if environment.resources["user acceptance tests passing"]:
        log.log_line("\t- Test successful!")
        environment.resources["stress"] -= 0.05
    else:
        log.log_line("\t- Test unsuccessful")
        log.log_line("\t- Rewriting tests")
        environment.resources["stress"] += 0.05

@atom
def attempt_deployment():
    log.log_line("Deploying product")
    environment.resources["stress"] += 0.1
    environment.resources["time"] -= 2
    environment.resources["successful deployment"] = random_boolean()
    if environment.resources["successful deployment"]:
        log.log_line("\t- Deployment successful!")
        environment.resources["tickets"] -= 1
        environment.resources["stress"] -= -0.1
    else:
        log.log_line("\t- Problems with building")
        log.log_line("\t- Rerunning integration test")

@atom
def gather_statistics_and_log():
    log.log_line("--------------------------------------------------------------------------------")
    log.log_line("Complete!")
    log.log_line()

    for key in environment.resources.keys():
        log.log_line(key + ":\t\t" + str(environment.resources[key]))
    log.log_line("--------------------------------------------------------------------------------")

