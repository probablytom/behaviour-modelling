import unittest, environment, sys, agile_flows, waterfall_flows, copy
from fuzzing_base import *

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

        print 2

        agile_flows.setup_environment()
        random.seed(environment.resources["seed"])
        environment.resources["mutating"] = False
        try:
            agile_flows.implement_50_features()
        except Exception, e:
            print str(e)
            self.assertTrue(False, str(e))
        agile_unmutated_results = copy.deepcopy(environment.resources)

        print 3

        waterfall_flows.setup_environment()
        random.seed(environment.resources["seed"])
        environment.resources["mutating"] = False
        try:
            waterfall_flows.implement_50_features()
        except Exception, e:
            print str(e)
            self.assertTrue(False, str(e))
        waterfall_unmutated_results = copy.deepcopy(environment.resources)

        print 4

        waterfall_flows.setup_environment()
        random.seed(environment.resources["seed"])
        environment.resources["mutating"] = True
        try:
            waterfall_flows.implement_50_features()
        except Exception, e:
            print str(e)
            self.assertTrue(False, str(e))
        waterfall_results = copy.deepcopy(environment.resources)

        print 5

        # Calculate some results. Which is more affected?
        agile_difference_under_stress = abs(agile_results["time"] - agile_unmutated_results["time"]) / float(agile_results["time"])
        waterfall_difference_under_stress = abs(waterfall_results["time"] - waterfall_unmutated_results["time"]) / float(waterfall_results["time"])

        self.assertLess(agile_difference_under_stress, waterfall_difference_under_stress)  # The hypothesis here is that Agile performs better than Waterfall


if __name__ == "__main__":
    sys.setrecursionlimit(10000000)
    unittest.main(verbosity=2)
