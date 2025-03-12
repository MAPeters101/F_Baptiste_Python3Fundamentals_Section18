'''
Question 3
Sometimes we have functions that get called often with the same argument
values but take a long time to run.

If those functions are deterministic (i.e. passing the same arguments will
always result in the same return value), then we can get a huge performance
benefit by implementing a caching mechanism.

This function simulates a long running function:

from time import sleep

def add(x, y):
    sleep(2)
    return x + y
As you can see the function is deterministic - the result will always be the
same for the same arguments.

Use Python's LRU caching decorator to help improve performance when this
function is called multiple times with the same arguments.

Then use timeit to test how performance is affected.
'''