from base import *
import inspect

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

test_comment()
print
test_truncate()
print
test_comment()
print
test_truncate()
print
test_truncate()
print
test_truncate()
print
test_truncate()
print
test_truncate()
print
print
print inspect.getsourcelines(test_truncate)
