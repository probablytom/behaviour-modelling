# Resources regarding the workflow's environment
time = 0 # to be incremented upon every step


# The resources we'll be editing
# NOTE: These should ordinarily be amended to reflect the project...
resources = {}
resources["stress"] = 0.1
resources["building"] = True
resources["money"] = 10000


# -----------------------------------------------------------------------------


# The functions that act as actions within the flowchart
def create_branch():
    pass

def write_tests():
    resources['money'] -= 100
    resources["stress"] += 0.1

def write_code():
    resources["money"] -= 100
    resources["stress"] += 0.05

def run_tests():
    resources["building"] = True  # TODO: To be changed by random int later
    resources["money"] -= 100
    if resources["building"]:
        resources["stress"] -= 0.1
    else:
        resources["stress"] += 0.1
        write_tests()


def integration_test():
    resources["money"] -= 100
    resources["building"] = True  # TODO: To be changed at random later
    if resources["building"]:
        resources["stress"] -= 0.05
    else:
        resources["stress"] += 0.05
        write_tests()

def merge():
    resources["money"] -= 100
    resources["stress"] += 0.05  # Because merging is always stressful, particularly with a large codebase. 
    # Perhaps this should scale to some "changes made" resource that gets incremented by the code and test writing?

def user_acceptance_test():
    resources["money"] -= 100
    resources["building"] = True  # TODO: To change by a random int later
    if resources["building"]:
        resources["stress"] -= 0.05
    else:
        resources["stress"] += 0.05
        write_tests()

def deploy():
    resources["stress"] += 0.1
    resources["money"] -= 100
    if not resources["building"]:
        integration_test()

def complete():
    print "--------------------------------------------------------------------------------"
    print "Complete!"

    for key in resources.keys():
        print key + ":\t\t" + str(resources[key])
    print "--------------------------------------------------------------------------------"


# -----------------------------------------------------------------------------


create_branch()
write_tests()
run_tests()
integration_test()
merge()
user_acceptance_test()
deploy()
complete()
