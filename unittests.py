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

    def test_mutation_randomness(self):
        mutation_randomness_test0()
        mutation_randomness_test1()
        self.assertNotEqual(results[0], results[1])
        
@mutate__comment_single_line
def mutation_randomness_test0():
    results[0] = 0
    results[0] += 1
    results[0] += 2
    results[0] += 3
    results[0] += 4
    results[0] += 5

@mutate__comment_single_line
def mutation_randomness_test_result1():
    results[1] = 0
    results[1] += 1
    results[1] += 2
    results[1] += 3
    results[1] += 4
    results[1] += 5

results = [0, 0, 0]

if __name__ == "__main__":
    unittest.main(verbosity = 2)
