import base, unittest, decorator_runtime_test, environment, sys, agile_flows, waterfall_flows
from base import *



class TestNewFlows(unittest.TestCase):

    def test_new_agile_model_completes(self):
        agile_flows.setup_environment()
        random.seed(environment.resources["seed"])
        try:
            agile_flows.implement_50_features()
        except Exception, e:
            print str(e)
        print environment.resources
        self.assertEqual(50, len(environment.resources["features"]))

    def test_new_waterfall_model_completes(self):
        waterfall_flows.setup_environment()
        random.seed(environment.resources["seed"])
        try:
            waterfall_flows.implement_50_features()
        except Exception, e:
            print str(e)
        print environment.resources
        self.assertEqual(50, environment.resources["size of product in features"])


@mutate(decorator_runtime_test.comment_single_line)
def mutation_randomness_test():
    results[0] = 0
    results[0] += 1
    results[0] += 2
    results[0] += 3
    results[0] += 4
    results[0] += 5

@mutate(decorator_runtime_test.truncate_function)
def mutation_truncation_example():
    results[1] = 0
    results[1] += 1
    results[1] += 2
    results[1] += 3
    results[1] += 4
    results[1] += 5

results = [0, 0, 0]

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    unittest.main(verbosity = 2)
