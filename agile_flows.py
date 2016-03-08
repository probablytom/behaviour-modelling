from software_engineering_atoms import *
from base import *
from decorators import flow, system_setup, metric
import environment

@system_setup
def setup_environment():
# The environment.resources we'll be editing
# NOTE: These should ordinarily be amended to reflect the initial state of the project...
    environment.resources = {}
    environment.resources["time"] = 0
    environment.resources["seed"] = 0
    environment.resources["integration tests passing"] = False
    environment.resources["user acceptance tests passing"] = False
    environment.resources["successful deployment"] = False
    environment.resources["code"] = []  # To be a list of Chunk objects
    environment.resources["bugs"] = []  # To be a list of Bug objects
    environment.resources["mutating"] = True
    environment.resources["current chunk"] = None
    environment.resources["current test"] = None
    environment.resources["current bug"] = None

def estimate_bugs():
    return environment.resources["lines of code"] / 15  # each 15 lines of code roughly causes a bug?

@flow
def write_code_using_tdd():
    write_tests()
    modify_code()

@flow
@mutate__comment_line_chance_20
def make_code_edit():
    write_code()
    run_tests()

@flow
def modify_code():
    make_code_edit()
    while not environment.resources["tests passing"]:
        make_code_edit()

@flow
def integration_testing_phase():
    integration_test()
    while not environment.resources["integration tests passing"]:
        modify_code()
        integration_test()

@flow
def testing():
    user_acceptance_test()
    while not environment.resources["user acceptance tests passing"]:
        modify_code()
        integration_testing_phase()
        user_acceptance_test()

@flow
def implement_feature():
    write_code_using_tdd()
    integration_testing_phase()
    user_acceptance_test()

@flow
def implement_50_features():
    for i in range(50):
        implement_feature()
        environment.resources["features implemented"] += 1

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
