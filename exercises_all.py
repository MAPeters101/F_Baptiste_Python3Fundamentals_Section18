'''
Question 1
Write a decorator that can be used to print out how long a function takes to run.

Question 2
We have several functions in our code that perform some calculations and return a numeric result, possibly float, int or even Decimal.

We actually want to make sure that all results from each of these functions are rounded to some number of digits after the decimal point (precision), and always returned as a float.

But every time our program runs, that precision could change. Also, we'd rather not have to change every function we have, since at some point in the future we may want to return Decimal objects, and not floats - so we want to minimize how much code we would have to change to accomodate all this.

For example, we might a variable in our code that defines the precision, and could be changed any time we run our code:

PRECISION = 2
Suppose we have the following functions already defined:

from decimal import Decimal

def perc_diff(x, y):
    try:
        return (y-x) / x * 100
    except ZeroDivisionError:
        return 0

def sum_squares(*args):
    return sum(x**2 for x in args)

def avg(*args):
    if len(args) == 0:
        return 0

    numbers = [Decimal(x) for x in args]
    sum_ = sum(numbers)
    return sum_ / len(numbers)
Write a decorator named normalize that can be used to decorate these functions to ensure that the result is always returned as a float with a precision defined by some global variable PRECISION.

Question 3
Sometimes we have functions that get called often with the same argument values but take a long time to run.

If those functions are deterministic (i.e. passing the same arguments will always result in the same return value), then we can get a huge performance benefit by implementing a caching mechanism.

This function simulates a long running function:

from time import sleep

def add(x, y):
    sleep(2)
    return x + y
As you can see the function is deterministic - the result will always be the same for the same arguments.

Use Python's LRU caching decorator to help improve performance when this function is called multiple times with the same arguments.

Then use timeit to test how performance is affected.

Question 4
This is kind of a "bonus" exercise. It's a follow-up to Question 2.

It's also complicated, so don't worry if you are unable to do this one!

In Question 2, we created a decorator that used a global variable for the precision.

Here, we would rather define a decorator that can take that precision as an argument, i.e. we could do something like this:

@normalize(2)
def perc_diff(x, y):
    try:
        return (y-x) / x * 100
    except ZeroDivisionError:
        return 0

@normalize(4)
def sum_squares(*args):
    return sum(x**2 for x in args)

@normalize(8)
def avg(*args):
    if len(args) == 0:
        return 0

    numbers = [Decimal(x) for x in args]
    sum_ = sum(numbers)
    return sum_ / len(numbers)
As a hint, remember how we created "partial" functions in a previous exercise?

What we'll want to do here is not write a decorator function directly, but instead write a function that will create a decorator function, with the precision captured in the decorator function (which will itself then, be a closure).

Something like this:

def normalize(precision):
    def decorator(fn):
        def inner(*args, **kwargs):
            # precision passed to normalize is available here
            return result
        return inner
    return decorator
'''