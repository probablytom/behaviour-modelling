from software_engineering_atoms import *
from decorators import flow, system_setup
import environment
from base import mutate

def random_boolean():
    return random.choice([True, False])


def stressed(lines):
    if random_boolean():
        lines.remove(random.choice(lines))
    return lines


def cannot_meet_deadline(lines):
    if random_boolean():
        lines = lines[:random.randint(1, len(lines)-1)]
    return lines


@system_setup
def setup_environment():
    # The environment.resources we'll be editing
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

    # Also reset the cache of the mutator
    mutate.reset()

@flow
def make_new_feature():
    create_feature()


@flow
@mutate(cannot_meet_deadline)
def create_test_and_code():
    create_test_tdd()
    add_chunk_tdd()
    print "test"


@flow
def unit_test():
    run_tests()
    while not environment.resources["unit tests passing"]:
        fix_recent_feature()
        run_tests()



@flow
def fix_recent_feature():
    for chunk in environment.resources["features"][-1]:
        fix_chunk(chunk)



@flow
def integration_test():
    perform_integration_tests()
    while not environment.resources["integration tests passing"]:
        unit_test()
        perform_integration_tests()


@flow
def user_acceptance_test():
    perform_user_acceptance_testing()
    while not environment.resources["user acceptance tests passing"]:
        unit_test()
        integration_test()
        perform_user_acceptance_testing()


@flow
def implement_feature():
    make_new_feature()
    create_test_and_code()
    unit_test()
    integration_test()
    user_acceptance_test()


@flow
def implement_50_features():
    for i in range(50):
        implement_feature()


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
