'''
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
'''