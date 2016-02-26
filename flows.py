from software_engineering_atoms import *
from base import *
from decorators import flow, system_setup, metric
import environment

@flow
@mutate__comment_line_chance_20
def modify_code():
    write_tests()
    write_code()
    run_tests()

@flow
def attempt_to_squash_bug():
    write_code_to_fix_bug()
    run_tests_on_bug()

@flow
@mutate__truncate_function
def squash_a_discovered_bug():
    begin_to_squash_bug()
    initial_problem_count = environment.resources["number of failing tests this iteration"]
    if initial_problem_count == environment.resources["number of failing tests this iteration"]:
        attempt_to_squash_bug()
    

@flow
def fix_failing_tests():
    if environment.resources["number of tests failing this iteration"] > 0:
        squash_a_discovered_bug()
        fix_failing_tests()

@flow
def check_code_is_working():
    if not environment.resources["tests passing"]:
        modify_code()
        check_code_is_working()

@flow
def implement_feature_using_ttd():
    modify_code()
    check_code_is_working()

@flow
def perform_integration_testing():
    integration_test()
    if not environment.resources["integration tests passing"]:
        modify_code()
        perform_integration_testing()

@flow
def perform_user_acceptance_testing():
    user_acceptance_test()
    if not environment.resources["user acceptance tests passing"]:
        make_changes()

@flow
def deploy():
    attempt_deployment()
    if not environment.resources["successful deployment"]:
        perform_integration_testing()
        deploy()  # see note 1

@flow
def finish_feature_implementation():
    gather_statistics_and_log()

@flow
def implement_new_feature():
    create_ticket()
    create_branch()
    make_changes()

@flow
def make_changes():
    checkout_branch()
    implement_feature_using_ttd()
    merge()
    perform_integration_testing()
    perform_user_acceptance_testing()
    deploy()
    finish_feature_implementation()

@flow
def implement_50_features():
    for i in range(50):
        implement_new_feature()
        additional_metric_evaluated()

@metric
def additional_metric_evaluated():
    environment.resources["features implemented"] += 1

@system_setup
def setup_environment():
# The environment.resources we'll be editing
# NOTE: These should ordinarily be amended to reflect the initial state of the project...
    environment.resources = {}
    environment.resources["stress"] = 0.05
    environment.resources["time"] = 1000
    environment.resources["tests passing"] = False
    environment.resources["integration tests passing"] = False
    environment.resources["user acceptance tests passing"] = False
    environment.resources["successful deployment"] = False
    environment.resources["tickets"] = 0
    environment.resources["branches"] = 1
    environment.resources["probability of bug being detected"] = 0.9
    environment.resources["number of tests"] = 0
    environment.resources["number of hidden bugs"] = 0
    environment.resources["number of bugs"] = 0
    environment.resources["lines of code"] = 1000  # We start with a fairly small codebase
    environment.resources["number of bugs added this iteration"] = 0
    environment.resources["tests to squash bug passing"] = False
    environment.resources["number of failing tests this iteration"] = 0
    environment.resources["current test passing"] = True
    environment.resources["features implemented"] = 0
    environment.resources["seed"] = 0
    environment.resources["mutating"] = True
# Should the number of tickets also be a record of bugs? (I'm inclined to say no)

def estimate_bugs():
    return environment.resources["lines of code"] / 15  # each 15 lines of code roughly causes a bug?

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
