from decorators import *

@mutate_comment_line
def test():
    print 1
    print 2
    print 3
    print 4
    print 5

@mutate_comment_line
def test_wont_work():
    for i in range(1, 6):
        print i

test()
print
test_wont_work()
