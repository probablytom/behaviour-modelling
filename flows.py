from software_engineering_atoms import *
from environment import resources
from base import *
from decorators import flow

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
    initial_problem_count = resources["number of failing tests this iteration"]
    if initial_problem_count == resources["number of failing tests this iteration"]:
        attempt_to_squash_bug()
    

@flow
def fix_failing_tests():
    if resources["number of tests failing this iteration"] > 0:
        squash_a_discovered_bug()
        fix_failing_tests()

@flow
def check_code_is_working():
    if not resources["tests passing"]:
        modify_code()
        check_code_is_working()

@flow
def implement_feature_using_ttd():
    modify_code()
    check_code_is_working()

@flow
def perform_integration_testing():
    integration_test()
    if not resources["integration tests passing"]:
        modify_code()
        perform_integration_testing()

@flow
def perform_user_acceptance_testing():
    user_acceptance_test()
    if not resources["user acceptance tests passing"]:
        make_changes()

@flow
def deploy():
    attempt_deployment()
    if not resources["successful deployment"]:
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
        resources["features implemented"] += 1
        print "feature " + str(i) + " implemented..."

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
