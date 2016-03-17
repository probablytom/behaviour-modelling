import unittest, environment, sys, agile_flows, waterfall_flows
from base import *


class TestNewFlows(unittest.TestCase):

    def test_new_agile_model_completes(self):
        agile_flows.setup_environment()
        random.seed(environment.resources["seed"])
        environment.resources["mutating"] = False
        try:
            agile_flows.implement_50_features()
        except Exception, e:
            print str(e)
        self.assertEqual(50, len(environment.resources["features"]))

    def test_new_waterfall_model_completes(self):
        waterfall_flows.setup_environment()
        random.seed(environment.resources["seed"])
        environment.resources["mutating"] = False
        try:
            waterfall_flows.implement_50_features()
        except Exception, e:
            print str(e)
        self.assertEqual(50, environment.resources["size of product in features"])

    def test_unittesting_mutation_stressed_waterfall(self):
        waterfall_flows.setup_environment()
        random.seed(environment.resources["seed"])
        try:
            waterfall_flows.implement_50_features()
        except Exception, e:
            print str(e)
            self.assertTrue(False)
        self.assertNotEqual(0, len(environment.resources["bugs"]))

    def test_unittesting_mutation_stressed_agile(self):
        agile_flows.setup_environment()
        random.seed(environment.resources["seed"])
        try:
            agile_flows.implement_50_features()
        except Exception, e:
            print str(e)
            self.assertTrue(False)
        self.assertNotEqual(0, len(environment.resources["bugs"]))

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    unittest.main(verbosity=2)
