import unittest, environment, sys, agile_flows, waterfall_flows, copy

import time

from fuzzing_base import *


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
            print str(e), " THIS IS AN ERROR"
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
import sys

def trace_calls_and_returns(frame, event, arg):
    co = frame.f_code
    func_name = co.co_name
    if func_name == 'write':
        # Ignore write() calls from print statements
        return
    line_no = frame.f_lineno
    filename = co.co_filename
    if event == 'call':
        print 'Call to %s on line %s of %s' % (func_name, line_no, filename)
        return trace_calls_and_returns
    elif event == 'return':
        print '%s => %s' % (func_name, arg)
    return

# sys.settrace(trace_calls_and_returns)

if __name__ == "__main__":
    sys.setrecursionlimit(10000000)
    unittest.main(verbosity=2)
