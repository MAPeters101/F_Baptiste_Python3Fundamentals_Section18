'''
Question 1
Write a decorator that can be used to print out how long a function takes to
run.

Solution
Let's start with the "standard" skeleton for a decorator.

def logged(f):
    def inner(*args, **kwargs):
        result = f(*args, **kwargs)
        return result
    return inner
Now, we just need to time and print out the timing before returning the result
of the function call.

from time import perf_counter

def logged(f):
    def inner(*args, **kwargs):
        start = perf_counter()
        result = f(*args, **kwargs)
        end = perf_counter()
        print(f'elapsed: {end - start} secs')
        return result
    return inner
And let's try it out on a few functions:

import math

@logged
def norm(x, y):
    return math.sqrt(x**2 + y**2)

@logged
def find_index_min(seq):
    min_ = min(seq)
    return seq.index(min_)
norm(3, 4)
find_index_min([3, 2, 1, 4, 5])
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

Solution
Let's start with the "standard" decorator skeleton.

def normalize(fn):
    def inner(*args, **kwargs):
        result = fn(*args, **kwargs)
        return result
    return inner
Next, we want to intercept the result, convert it to a float, and round it to
PRECISION.

def normalize(fn):
    def inner(*args, **kwargs):
        result = fn(*args, **kwargs)
        result = round(float(result), PRECISION)
        return result
    return inner
Now we can apply this decorator our functions:

from decimal import Decimal

PRECISION = 2

@normalize
def perc_diff(x, y):
    try:
        return (y-x) / x * 100
    except ZeroDivisionError:
        return 0

@normalize
def sum_squares(*args):
    return sum(x**2 for x in args)

@normalize
def avg(*args):
    if len(args) == 0:
        return 0

    numbers = [Decimal(x) for x in args]
    sum_ = sum(numbers)
    return sum_ / len(numbers)
And let's try them out:

perc_diff(13, 16)
sum_squares(0.1, 0.2, 0.3)
avg(1.1, 3.14, 42)
The nice thing about that approach, is that we can easily change the precision
before running our code without changing any of our code except the value of
PRECISION:

from decimal import Decimal

PRECISION = 6

@normalize
def perc_diff(x, y):
    try:
        return (y-x) / x * 100
    except ZeroDivisionError:
        return 0

@normalize
def sum_squares(*args):
    return sum(x**2 for x in args)

@normalize
def avg(*args):
    if len(args) == 0:
        return 0

    numbers = [Decimal(x) for x in args]
    sum_ = sum(numbers)
    return sum_ / len(numbers)

print(perc_diff(13, 16))
print(sum_squares(0.1, 0.2, 0.3))
print(avg(1.1, 3.14, 42))
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

Solution
We'll use the lru_cache decorator that is in the functools module:

from functools import lru_cache
Let's see how our function runs before we use the cache:

from timeit import timeit

timeit('add(2, 2)', globals=globals(), number=10)
20.022507932
As expected, this took 20 seconds to run.

Now let's decorate that add function:

@lru_cache
def add(x, y):
    sleep(2)
    return x + y
And let's run the timings again:

timeit('add(2, 2)', globals=globals(), number=10)
2.0038045129999986
Question 4
This is kind of a "bonus" exercise. It's a follow-up to Question 2.

It's also complicated, so don't worry if you are unable to do this one!

In Question 2, we created a decorator that used a global variable for the
precision.

Here, we would rather define a decorator that can take that precision as an
argument, i.e. we could do something like this:

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

What we'll want to do here is not write a decorator function directly, but
instead write a function that will create a decorator function, with the
precision captured in the decorator function (which will itself then, be a
closure).

Something like this:

def normalize(precision):
    def decorator(fn):
        def inner(*args, **kwargs):
            # precision passed to normalize is available here
            return result
        return inner
    return decorator
Solution
Looking at that skeleton above, you'll notice that when normalize(precision is
called, it actually returns... a decorator. The difference here is that that
decorator also has access to precision - i.e. a closure.

Let's implement this:

def normalize(precision):
    def decorator(fn):
        def inner(*args, **kwargs):
            result = fn(*args, **kwargs)
            return round(float(result), precision)
        return inner
    return decorator
Let's call normalize and see what we get - remember that the return value is a
function that is a decorator.

dec_normalize_2 = normalize(2)
dec_normalize_10 = normalize(10)
We can inspect these closures to see what the free variables are in each:

dec_normalize_2.__closure__
(<cell at 0x7fd6f827a1c0: int object at 0x7fd73800e950>,)
That integer is actually the integer 2:

hex(id(2))
'0x7fd73800e950'
And the same with dec_normalize_10:

dec_normalize_10.__closure__
(<cell at 0x7fd6f827a100: int object at 0x7fd73800ea50>,)
hex(id(10))
'0x7fd73800ea50'
And now we can decorate our functions using this decorator "factory":

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
perc_diff(13, 42)
223.08
sum_squares(0.01, 0.02, 0.03)
0.0014
avg(1.1, 2.2, 3.14)
2.14666667
And this is how "parametrized" decorators can be created in general - we are
basically creating and returning generators from a "factory" function.
'''