import unittest, environment, sys, agile_flows, waterfall_flows, copy
from base import *


class TestVariance(unittest.TestCase):

    def test_compare_agile_waterfall_with_variance(self):

        # Carry out the simulation with and without mutation, and see whether one takes much longer than another
        agile_flows.setup_environment()
        random.seed(environment.resources["seed"])
        environment.resources["mutating"] = True
        try:
            agile_flows.implement_50_features()
        except Exception, e:
            print str(e)
            self.assertTrue(False, str(e))
        agile_results = copy.deepcopy(environment.resources)

        agile_flows.setup_environment()
        random.seed(environment.resources["seed"])
        environment.resources["mutating"] = False
        try:
            agile_flows.implement_50_features()
        except Exception, e:
            print str(e)
            self.assertTrue(False, str(e))
        agile_unmutated_results = copy.deepcopy(environment.resources)

        waterfall_flows.setup_environment()
        random.seed(environment.resources["seed"])
        environment.resources["mutating"] = False
        try:
            waterfall_flows.implement_50_features()
        except Exception, e:
            print str(e)
            self.assertTrue(False, str(e))
        waterfall_unmutated_results = copy.deepcopy(environment.resources)

        waterfall_flows.setup_environment()
        random.seed(environment.resources["seed"])
        environment.resources["mutating"] = True
        try:
            waterfall_flows.implement_50_features()
        except Exception, e:
            print str(e)
            self.assertTrue(False, str(e))
        waterfall_results = copy.deepcopy(environment.resources)

        # Calculate some results. Which is more affected?
        agile_difference_under_stress = abs(agile_results["time"] - agile_unmutated_results["time"]) / float(agile_results["time"])
        waterfall_difference_under_stress = abs(waterfall_results["time"] - waterfall_unmutated_results["time"]) / float(waterfall_results["time"])

        self.assertLess(agile_difference_under_stress, waterfall_difference_under_stress)  # The hypothesis here is that Agile performs better than Waterfall


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
