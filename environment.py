# The resources we'll be editing

def probability_of_bug_detection():
    lines_covered = resources["number of tests"] * resources["average test coverage in lines of code"]
    lines_covered = min(lines_covered, resources["lines of code"])
    return float(lines_covered) / resources["lines of code"]

def coverage_rate():
    lines_covered = resources["number of tests"] * resources["average test coverage in lines of code"]
    lines_covered = min(lines_covered, resources["lines of code"])
    return float(lines_covered) / resources["lines of code"]


resources = {}
resources["stress"] = 0.05
resources["time"] = 200
resources["tests passing"] = False
resources["integration tests passing"] = False
resources["user acceptance tests passing"] = False
resources["successful deployment"] = False
resources["tickets"] = 0
resources["branches"] = 1
resources["probability of bug being detected"] = probability_of_bug_detection
resources["number of tests"] = 25
resources["number of hidden bugs"] = 0
resources["number of bugs"] = 0
resources["lines of code"] = 1000  # We start with a fairly small codebase
resources["number of bugs added this iteration"] = 0
resources["tests to squash bug passing"] = False
resources["number of failing tests this iteration"] = 0
resources["current test passing"] = True
resources["features implemented"] = 0
resources["seed"] = 0
resources["average test coverage in lines of code"] = 30
resources["mutating"] = True
# Should the number of tickets also be a record of bugs? (I'm inclined to say no)

