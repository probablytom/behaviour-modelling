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
resources["time"] = 0
resources["seed"] = 0
resources["integration tests passing"] = False
resources["user acceptance tests passing"] = False
resources["unit tests passing"] = False
resources["tests"] = []
resources["successful deployment"] = False
resources["features"] = []  # To be a list of Chunk objects
resources["bugs"] = []  # To be a list of Bug objects
resources["mutating"] = True
resources["current chunk"] = None
resources["most recent test"] = None
resources["current bug"] = None
resources["current feature"] = 0

