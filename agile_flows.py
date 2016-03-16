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
    environment.resources["unit tests passing"] = False
    environment.resources["successful deployment"] = False
    environment.resources["features"] = []  # To be a list of Chunk objects
    environment.resources["bugs"] = []  # To be a list of Bug objects
    environment.resources["tests"] = []
    environment.resources["mutating"] = True
    environment.resources["current chunk"] = None
    environment.resources["most recent test"] = None
    environment.resources["current bug"] = None
    environment.resources["current feature"] = 0

@flow
def make_new_feature():
    print "making feature"
    create_feature()

def implement_code():
    print "implementing code"
    create_test_tdd()
    add_chunk_tdd()

def unit_test():
    print "unit testing"
    run_tests()
    while not environment.resources["unit tests passing"]:
        fix_recent_feature()
        run_tests()


def fix_recent_feature():
    print "fixing recent feature"
    for chunk in environment.resources["features"][-1]:
        fix_chunk(chunk)


def integration_test():
    print "integration testing"
    perform_integration_tests()
    while not environment.resources["integration tests passing"]:
        unit_test()
        perform_integration_tests()

def user_acceptance_test():
    print "UA testing"
    perform_user_acceptance_testing()
    while not environment.resources["user acceptance tests passing"]:
        unit_test()
        integration_test()
        perform_user_acceptance_testing()


@flow
def implement_feature():
    make_new_feature()
    implement_code()
    unit_test()
    integration_test()
    user_acceptance_test()
    print "implemented feature " + str(len(environment.resources["features"]))


@flow
def implement_50_features():
    for i in range(50):
        implement_feature()
        print "implemented " + str(i)


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
