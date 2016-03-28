import unittest, environment, sys, agile_flows, waterfall_flows, copy
from fuzzing_base import *


class TestVariance(unittest.TestCase):

    def test_multiple_seed_average(self):

        agile_results = [[],[]]
        waterfall_results = [[],[]]

        seed = 0

        for i in range(8):
            agile_flows.setup_environment()
            random.seed(environment.resources["seed"])
            environment.resources["mutating"] = i % 2 == 1
            seed += 50
            environment.resources["seed"] = seed
            try:
                agile_flows.implement_50_features()
            except Exception, e:
                print str(e)
                self.assertTrue(False, str(e))
            agile_results[i%2].append(copy.deepcopy(environment.resources))

        seed = 0

        for i in range(8):
            waterfall_flows.setup_environment()
            random.seed(environment.resources["seed"])
            environment.resources["mutating"] = i % 2 == 1
            seed += 50
            environment.resources["seed"] = seed
            try:
                waterfall_flows.implement_50_features()
            except Exception, e:
                print str(e)
                self.assertTrue(False, str(e))
            waterfall_results[i%2].append(copy.deepcopy(environment.resources))

        # Calculate some results. Which is more affected?
        agile_aggregate_times = [0, 0]
        waterfall_aggregate_times = [0, 0]

        for i in range(4):
            agile_aggregate_times[0] += agile_results[0][i]["time"]
            agile_aggregate_times[1] += agile_results[1][i]["time"]
        for i in range(4):
            waterfall_aggregate_times[0] += waterfall_results[0][i]["time"]
            waterfall_aggregate_times[1] += waterfall_results[1][i]["time"]

        agile_average_times = [0,0]
        waterfall_average_times = [0,0]

        agile_average_times[0] = agile_aggregate_times[0]/4
        agile_average_times[1] = agile_aggregate_times[1]/4
        waterfall_average_times[0] = waterfall_aggregate_times[0]/4
        waterfall_average_times[1] = waterfall_aggregate_times[1]/4

        agile_delta = abs(agile_average_times[1] - agile_average_times[0])
        waterfall_delta = abs(waterfall_average_times[1] - waterfall_average_times[0])

        agile_delta /= float(agile_average_times[0])
        waterfall_delta /= float(waterfall_average_times[0])

        self.assertNotAlmostEqual(agile_delta, waterfall_delta, delta=agile_delta*0.1)
        self.assertLess(agile_delta, waterfall_delta)


class CompareMutantVariance(unittest.TestCase):

    def test_new_agile_model_completes(self):
        agile_flows.setup_environment()
        random.seed(environment.resources["seed"])
        environment.resources["mutating"] = False
        try:
            agile_flows.implement_50_features()
        except Exception, e:
            print str(e)
            self.assertTrue(False, str(e))
        self.assertEqual(50, len(environment.resources["features"]))

    def test_new_waterfall_model_completes(self):
        waterfall_flows.setup_environment()
        random.seed(environment.resources["seed"])
        environment.resources["mutating"] = False
        try:
            waterfall_flows.implement_50_features()
        except Exception, e:
            print str(e)
            self.assertTrue(False, str(e))
        self.assertEqual(50, environment.resources["size of product in features"])

    def test_unittesting_mutation_stressed_waterfall(self):
        waterfall_flows.setup_environment()
        random.seed(environment.resources["seed"])
        environment.resources["mutating"] = True
        try:
            waterfall_flows.implement_50_features()
        except Exception, e:
            print str(e)
            self.assertTrue(False, str(e))
        mutated_results = copy.deepcopy(environment.resources)

        waterfall_flows.setup_environment()
        random.seed(environment.resources["seed"])
        environment.resources["mutating"] = False
        try:
            waterfall_flows.implement_50_features()
        except Exception, e:
            print str(e)
            self.assertTrue(False, str(e))
        unmutated_results = copy.deepcopy(environment.resources)

        # Are the mutated results within a 10% margin of the unmutated results?
        self.assertNotAlmostEqual(unmutated_results["time"], mutated_results["time"], delta=unmutated_results["time"]*.1)


    def test_unittesting_mutation_stressed_agile(self):
        # Carry out the simulation with and without mutation, and see whether one takes much longer than another
        agile_flows.setup_environment()
        random.seed(environment.resources["seed"])
        environment.resources["mutating"] = True
        try:
            agile_flows.implement_50_features()
        except Exception, e:
            print str(e)
            self.assertTrue(False, str(e))
        mutated_results = copy.deepcopy(environment.resources)

        agile_flows.setup_environment()
        random.seed(environment.resources["seed"])
        environment.resources["mutating"] = False
        try:
            agile_flows.implement_50_features()
        except Exception, e:
            print str(e)
            self.assertTrue(False, str(e))
        unmutated_results = copy.deepcopy(environment.resources)

        # Are the mutated results within a 10% margin of the unmutated results?
        self.assertNotAlmostEqual(unmutated_results["time"], mutated_results["time"],
                                  delta=unmutated_results["time"]*.1)



if __name__ == "__main__":
    sys.setrecursionlimit(10000000)
    unittest.main(verbosity=2)
