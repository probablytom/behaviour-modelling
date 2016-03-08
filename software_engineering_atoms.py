import random, environment, dag
from logger import Logger
from decorators import atom, atom_args  # Will need renaming

# For keeping a log / printing to the console
# filepath-----\/           Logging--\/   printing--\/
log = Logger(   "event.log",         False,           False)

# -----------------------------------------------------------------------------
# HELPER FUNCTIONS
# -----------------------------------------------------------------------------




# -----------------------------------------------------------------------------
# LOW LEVEL ACTIONS
# atomic activity for actual activity within the sociotechnical system
# all interactions with environment.resources, shouldn't be anything else...
# -----------------------------------------------------------------------------


@atom
def add_chunk(testing=False):

    # Creating code takes time!
    environment.resources["time"] += 2

    # Create the chunk and add it to our environment
    new_chunk = dag.Chunk(testing)
    environment.resources["code"].add(new_chunk)
    environment.resources["current chunk"] = new_chunk
    # Is the chunk we just made afflicted with a bug in existing code?
    if environment.resources["bugs"] is not []:
        for i in range(random.randint(0, 1)):
            random.choice(environment.resources["bugs"]).add_adjacent(new_chunk)  # Add chunk to old bug if needed

    # Does the chunk we just made contain bugs?
    for i in range(random.randint(0, 3)):
        new_bug = dag.Bug(new_chunk)
        environment.resources["bugs"].append(new_bug)


@atom
def make_test_for_chunk(chunk=None):
    if chunk is None: chunk = environment.resources["current chunk"]
    new_test = dag.Test(chunk)
    chunk.set_test(new_test)

    # Creating a test takes time!
    environment.resources["time"] += 1


@atom
def fix_chunk(chunk=None):
    if chunk is None: chunk = environment.resources["current chunk"]
    for bug in chunk.adjacences():
        if random.choice([True, False]):  # Randomly correct the problem
            chunk.remove_adjacent(bug)
            # If this bug is fixed, remove it from all other afflicted classes too!
            for other_chunk in environment.resources["code"]:
                if bug in other_chunk.adjacences():
                    other_chunk.remove_adjacent(bug)
            # Bug is fixed so it should also be removed from our list of bugs
            environment.resources["bugs"].remove(bug)
            chunk.

