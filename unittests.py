import base, unittest, decorator_runtime_test, environment, flows, sys
from base import *


class TestMutationRandomness(unittest.TestCase):
    def test_mutation_comment(self):
        decorator_runtime_test.results = [0,0,0]
        decorator_runtime_test.add_15_normal()
        decorator_runtime_test.add_15_comment()
        self.assertNotEqual(decorator_runtime_test.results[0], decorator_runtime_test.results[2])

    def test_mutation_truncate(self):
        decorator_runtime_test.results = [0,0,0]
        decorator_runtime_test.add_15_normal()
        decorator_runtime_test.add_15_truncate()
        self.assertNotEqual(decorator_runtime_test.results[1], decorator_runtime_test.results[2])

    def test_mutation_randomness(self):
        random.seed(20)
        mutation_randomness_test()
        first_result = results[0]
        random.seed(0)
        mutation_randomness_test()
        second_result = results[0]
        self.assertNotEqual(first_result, second_result)

    def test_mutation_truncation(self):
        mutation_truncation_example()
        first_result = results[1]
        mutation_truncation_example()
        second_result = results[1]
        self.assertNotEqual(first_result, second_result)

class TestModelEmergentPhenomena(unittest.TestCase):
    def test_model_instances(self):
        flows.setup_environment()
        try:
            flows.implement_50_features()
        except:
            pass
        first_results = environment.resources
        flows.setup_environment()
        environment.resources["seed"] = 1000  # Change the seed so we're changing the mutations.
        try:
            flows.implement_50_features()
        except:
            pass
        second_results = environment.resources
        print first_results, '\n', second_results
        self.assertNotEqual(first_results["features implemented"], second_results["features implemented"])

@mutate__comment_single_line
def mutation_randomness_test():
    results[0] = 0
    results[0] += 1
    results[0] += 2
    results[0] += 3
    results[0] += 4
    results[0] += 5

@mutate__truncate_function
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
