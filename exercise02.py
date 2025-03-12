'''
Question 2
We have several functions in our code that perform some calculations and
return a numeric result, possibly float, int or even Decimal.

We actually want to make sure that all results from each of these functions
are rounded to some number of digits after the decimal point (precision), and
always returned as a float.

But every time our program runs, that precision could change. Also, we'd
rather not have to change every function we have, since at some point in the
future we may want to return Decimal objects, and not floats - so we want to
minimize how much code we would have to change to accomodate all this.

For example, we might a variable in our code that defines the precision, and
could be changed any time we run our code:

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
Write a decorator named normalize that can be used to decorate these functions
to ensure that the result is always returned as a float with a precision
defined by some global variable PRECISION.
'''