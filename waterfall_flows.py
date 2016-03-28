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
    environment.resources["tests"] = []  # To be a list of Test objects
    environment.resources["mutating"] = True
    environment.resources["current chunk"] = None
    environment.resources["current test"] = None
    environment.resources["current bug"] = None
    environment.resources["size of product in features"] = None
    environment.resources["features implemented"] = 0

    # Also reset the cache of the mutator
    # mutate.reset()


@flow
def write_code():
    add_chunk_waterfall()


@flow
def unit_test():
    for chunk in environment.resources["features"]:
        if chunk.test is None: create_test_for_chunk(chunk)
    run_tests()
    while not environment.resources["unit tests passing"]:
        fix_codebase()
        run_tests()


@flow
def fix_codebase():
    for test in environment.resources["tests"]:
        if not test_passes(test):
            fix_chunk(test.chunk)


@flow
def integration_test():
    perform_integration_tests()
    while not environment.resources["integration tests passing"]:
        fix_codebase()
        perform_integration_tests()


@flow
def user_acceptance_test():
    perform_integration_tests()
    while not environment.resources["integration tests passing"]:
        fix_codebase()
        perform_integration_tests()
        integration_test()


@flow
@mutate(stressed)
def create_product():
    for i in range(environment.resources["size of product in features"]):
        write_code()
    for i in range(environment.resources["size of product in features"]):
        unit_test()
    for i in range(environment.resources["size of product in features"]):
        integration_test()
    for i in range(environment.resources["size of product in features"]):
        user_acceptance_test()


@flow
def implement_50_features():
    environment.resources["size of product in features"] = 50
    create_product()


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
