import base, unittest, decorator_runtime_test

class TestMutationRandomness(unittest.TestCase):
    def test_mutation_comment(self):
        decorator_runtime_test.results = [0,0,0]
        decorator_runtime_test.add_15_normal()
        decorator_runtime_test.add_15_comment()
        print decorator_runtime_test.results
        self.assertNotEqual(decorator_runtime_test.results[0], decorator_runtime_test.results[2])

    def test_mutation_truncate(self):
        decorator_runtime_test.results = [0,0,0]
        decorator_runtime_test.add_15_normal()
        decorator_runtime_test.add_15_truncate()
        print decorator_runtime_test.results
        self.assertNotEqual(decorator_runtime_test.results[1], decorator_runtime_test.results[2])

if __name__ == "__main__":
    unittest.main(verbosity = 2)
