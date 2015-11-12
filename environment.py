# The resources we'll be editing
# NOTE: These should ordinarily be amended to reflect the initial state of the project...
resources = {}
resources["stress"] = 0.05
resources["money"] = 1000000
resources["tests passing"] = False
resources["integration tests passing"] = False
resources["user acceptance tests passing"] = False
resources["successful deployment"] = False
resources["tickets"] = 0
resources["branches"] = 1
resources["probability of bugs being detected"] = 0.1
resources["number of tests"] = 0
resources["number of hidden bugs"] = 0
resources["number of bugs"] = 0
#resources["estimated total number of bugs"] = estimate_bugs
resources["lines of code"] = 1000  # We start with a fairly small codebase
resources["number of bugs added this iteration"] = 0
resources["tests to squash bug passing"] = False
resources["number of failing tests this iteration"] = 0
resources["current test passing"] = True

# Should the number of tickets also be a record of bugs? (I'm inclined to say no)

def estimate_bugs():
    return resources["lines of code"] / 15  # each 15 lines of code roughly causes a bug?
