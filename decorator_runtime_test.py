from base import *

import inspect

@mutate__comment_single_line
def add_15_comment():
    results[0] += 1
    results[0] += 2
    results[0] += 3
    results[0] += 4
    results[0] += 5

@mutate__truncate_function
def add_15_truncate():
    results[1] += 1
    results[1] += 2
    results[1] += 3
    results[1] += 4
    results[1] += 5

def add_15_normal():
    results[2] += 1
    results[2] += 2
    results[2] += 3
    results[2] += 4
    results[2] += 5


def comment_single_line_mutation(lines):
    lines.remove(random.choice(lines))
    return lines


@mutate(comment_single_line_mutation)
def mutation_parameterisation_test():
    results[0] = 0
    results[0] += 1
    results[0] += 2
    results[0] += 3
    results[0] += 4
    results[0] += 5


@mutate__comment_single_line
def test_comment():
    print 1 
    print 2 
    print 3  
    print 4
    print 5

@mutate__truncate_function
def test_truncate():
    print "the"
    print "quick"
    print "brown"
    print "fox"
    print "jumps"
    print "over"
    print "the"
    print "lazy"
    print "mutation"

if __name__ == "__main__":
    test_truncate()
    print
    test_comment()
    print
    test_comment()
    print
    test_truncate()
    print
    test_comment()
    print
    test_truncate()
    print
    test_comment()
    print
    test_truncate()

results = [0, 0, 0]
