import base, unittest, decorator_runtime_test, environment, flows
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
        mutation_randomness_test()
        first_result = results[0]
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
        initial_environment = environment.resources
        flows.implement_50_features()
        first_results = environment.resources
        environment.resources = initial_environment
        environment.resources["seed"] = 100  # Change the seed so we're changing the mutations.
        flows.implement_50_features()
        second_results = environment.resources
        self.assertNotEqual(first_results, second_results)

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
    unittest.main(verbosity = 2)
