import random, environment, dag
from logger import Logger
from decorators import atom, atom_args  # Will need renaming
from base import atom_args

# For keeping a log / printing to the console
# filepath-----\/           Logging--\/   printing--\/
log = Logger(   "event.log",         False,           False)

# -----------------------------------------------------------------------------
# HELPER FUNCTIONS
# -----------------------------------------------------------------------------

def is_tested(chunk):
    for test in environment.resources["tests"]:
        if test.chunk() is chunk: return True
    return False


def has_bug(chunk):
    for bug in environment.resources["bugs"]:
        if chunk in bug.chunks(): return True
    return False


def detects_bug(test, bug):
    return test.chunk in bug.chunks and test.works


def bug_found(bug):
    for test in environment.resources["tests"]:
        if detects_bug(test, bug): return True
    return False

def get_feature_of_chunk(chunk):
    for feature in range(environment.resources["features"]):
        if chunk in environment.resources["features"][feature]: return feature
    return None

def test_passes(test):
    for bug in environment.resources["bugs"]:
        if detects_bug(test, bug): return True
    return False

def remove_bug(bug):
    print "1"
    environment.resources["bugs"].remove(bug)
    print "2"

def cost_of_bug(bug):
    return bug.age() / 20 + 1

def number_of_detected_bugs():
    n = 0
    for bug in environment.resources["bugs"]:
        for test in environment.resources["tests"]:
            if detects_bug(test, bug):
                n += 1
                break
    return n


# -----------------------------------------------------------------------------
# LOW LEVEL ACTIONS
# atomic activity for actual activity within the sociotechnical system
# all interactions with environment.resources, shouldn't be anything else...
# -----------------------------------------------------------------------------

@atom
def create_feature():
    environment.resources["features"].append([])
    environment.resources["current feature"] = len(environment.resources["features"])-1


# TODO: Potentially add currently existing bugs to this
# TODO: Simulate tests that are ineffective
@atom
def add_chunk(testing=False):
    print "Adding chunk"
    environment.resources["time"] += 2
    feature = environment.resources["current feature"]
    chunk = dag.Chunk()

    # Add a test if it's necessary
    if testing:
        test = environment.resources["tests"][-1]
        chunk.test = test
        test.chunk = chunk
        environment.resources["tests"].append(test)

    # Record this chunk of code
    environment.resources["features"][feature].append(chunk)

    # Conditionally add a bug to the chunk
    if random.randint(3,5) is 4:
        bug = dag.Bug(chunk)
        environment.resources["bugs"].append(bug)

    # We're now working on the chunk we just created, so...
    environment.resources["current chunk"] = chunk


# TODO: Potentially add currently existing bugs to this
# TODO: Simulate tests that are ineffective
@atom
def add_chunk_waterfall(testing=False):
    print "Adding chunk"
    environment.resources["time"] += 2
    chunk = dag.Chunk()

    # Add a test if it's necessary
    if testing:
        test = environment.resources["tests"][-1]
        chunk.test = test
        test.chunk = chunk
        environment.resources["tests"].append(test)

    # Record this chunk of code
    environment.resources["features"].append(chunk)

    # Conditionally add a bug to the chunk
    if random.randint(3,5) is 4:
        bug = dag.Bug(chunk)
        environment.resources["bugs"].append(bug)

    # We're now working on the chunk we just created, so...
    environment.resources["current chunk"] = chunk


# TODO: Potentially add currently existing bugs to this
# TODO: Simulate tests that are ineffective
@atom
def add_chunk_tdd(testing=True):
    environment.resources["time"] += 2
    feature = environment.resources["current feature"]
    chunk = dag.Chunk()

    # Add a test if it's necessary
    if testing:
        test = environment.resources["tests"][-1]
        if test is not None:
            chunk.test = test
            test.chunk = chunk
            environment.resources["tests"].append(test)

    # Record this chunk of code
    environment.resources["features"][feature].append(chunk)

    # Conditionally add a bug to the chunk
    if random.randint(3,5) is 4:
        bug = dag.Bug(chunk)
        environment.resources["bugs"].append(bug)

    # We're now working on the chunk we just created, so...
    environment.resources["current chunk"] = chunk


@atom
def create_test_for_chunk(chunk):
    environment.resources["time"] += 1
    if chunk.test is None:
        test = dag.Test(chunk)
        environment.resources["tests"].append(test)

def create_test_tdd():
    environment.resources["time"] += 1
    test = dag.Test()
    environment.resources["tests"].append(test)


@atom
def fix_chunk(chunk=None):
    if chunk is None: chunk = environment.resources["current chunk"]

    # Iterate over bugs that affect the chunk and thrash until fixed
    # TODO: Do this without actually thrashing...?
    print environment.resources["bugs"]
    for bug in environment.resources["bugs"]:
        while detects_bug(chunk.test, bug):
            environment.resources["time"] += cost_of_bug(bug)
            if random.randint(0, 5) is 4:
                remove_bug(bug)
                break


@atom
def perform_integration_tests():
    if len(environment.resources["bugs"]) == 0:
        environment.resources["integration tests passing"] = True
        return True
    number_of_messy_bugs = random.randint(0,len(environment.resources["bugs"]))
    environment.resources["integration tests passing"] = number_of_messy_bugs == 0

    return environment.resources["integration tests passing"]


@atom
def run_tests():
    environment.resources["unit tests passing"] = number_of_detected_bugs() == 0
    return environment.resources["unit tests passing"]


# TODO: Don't expect behaviour driven tests (because then passing tests != happy users)
@atom
def perform_user_acceptance_testing():
    print 1
    environment.resources["time"] += 1
    print 2
    environment.resources["user acceptance tests passing"] = environment.resources["unit tests passing"]
    return environment.resources["user acceptance tests passing"]


