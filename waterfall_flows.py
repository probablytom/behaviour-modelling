from software_engineering_atoms import *
from base import *
from decorators import flow, system_setup, metric
import environment

@system_setup
def setup_environment():
# The environment.resources we'll be editing
# NOTE: These should ordinarily be amended to reflect the initial state of the project...
    environment.resources = {}
    environment.resources["stress"] = 0.05
    environment.resources["time"] = 200
    environment.resources["tests passing"] = False
    environment.resources["integration tests passing"] = False
    environment.resources["user acceptance tests passing"] = False
    environment.resources["successful deployment"] = False
    environment.resources["tickets"] = 0
    environment.resources["branches"] = 1
    environment.resources["probability of bug being detected"] = environment.probability_of_bug_detection
    environment.resources["number of tests"] = 0
    environment.resources["number of hidden bugs"] = 0
    environment.resources["number of bugs"] = 0
    environment.resources["lines of code"] = 1000  # We start with a fairly small codebase
    environment.resources["number of bugs added this iteration"] = 0
    environment.resources["tests to squash bug passing"] = False
    environment.resources["number of failing tests this iteration"] = 0
    environment.resources["current test passing"] = True
    environment.resources["features implemented"] = 0
    environment.resources["seed"] = 0
    environment.resources["mutating"] = True
    environment.resources["average test coverage in lines of code"] = 10
# Should the number of tickets also be a record of bugs? (I'm inclined to say no)

@flow
def implement_feature():
    write_code()

@flow
def coding():
    # Implements 10 features
    for i in range(0, 10):
        implement_feature()

@flow
def unit_test():
    write_tests()
    run_tests()
    if environment.resources["tests passing"] == False:
        debug()
        unit_test()

@flow
def debug():
    write_code()
    run_tests()

@mutate__comment_line_chance_20
@flow
def integration_testing():
    run_integration_tests()
    if environment.resources["integration tests passing"]:
        unit_test()
        integration_testing()

@flow
def test():
    user_acceptance_test()
    while not environment.resources["user acceptance tests passing"]:
        reimplement_feature()
        unit_test()
        integration_test()
        user_acceptance_test()

@flow
def reimplement_feature():
    write_code()

# Implements 10 features
@flow
def create_major_version():
    coding()
    unit_test()
    integration_test()
    test()

@flow
def implement_50_features():
    for i in range(0, 5):
        create_major_version()
        environment.resources["features implemented"] += 10

def estimate_bugs():
    return environment.resources["lines of code"] / 15  # each 15 lines of code roughly causes a bug?

'''
NOTE 1
In the flowchart, one also goes through user acceptance testing again.
This isn't realistic, though, because the feature is the same, and the difference is the underlying
    implementation, which wouldn't affect U/A
So do we strictly follow a flowchart or UML activity diagram?
There are benefits to moving away from that model.
Also, moving away from this allows for us to more elegantly fix the problems with doing this procedurally:
  - We can intelligently act on state
  - We can avoid rerunning atoms due to recursive calls
  - We can be more specific with our specification of flow
'''
