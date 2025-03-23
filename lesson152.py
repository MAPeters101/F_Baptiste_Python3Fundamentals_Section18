
def cache(func):
    def inner(*args):
        result = func(*args)
        return result
    return inner

cache_dict = {}
def cache(func):
    def inner(*args):
        if args in cache_dict:
            return cache_dict[args]
        else:
            result = func(*args)
            cache_dict[args] = result
            return result
    return inner

@cache
def add(a, b):
    return a+b

@cache
def mult(a, b):
    return a*b

print(add(1,2))
print(cache_dict)

print(mult(1,2))
print(cache_dict)
print('-'*80)

def cache(func):
    def inner(*args):
        print('initializing cache...')
        cache_dict = {}
        if args in cache_dict:
            return cache_dict[args]
        else:
            result = func(*args)
            cache_dict[args] = result
            return result
    return inner

@cache
def add(a, b):
    return a+b

print(add(1,2))
print(cache_dict)
print()
print(add(1,2))
print(cache_dict)

print('-'*80)

def cache(func):
    print('initializing cache...')
    cache_dict = {}
    def inner(*args):
        if args in cache_dict:
            print('cache hit')
            return cache_dict[args]
        else:
            print('cache miss')
            result = func(*args)
            cache_dict[args] = result
            return result
    return inner

@cache
def add(a, b):
    print('add running')
    return a+b

@cache
def mult(a, b):
    print('mult running')
    return a*b

print(add.__closure__)
print(mult.__closure__)
print('-'*80)

print(add(1,2))
print(add(1,2))
print(add(2,3))
print(add(1,2))
print(add(2,3))
print('-'*80)

print(mult(1,2))
print(mult(3,4))
print(mult(1,2))
print(mult(3,4))
print('-'*80)

from functools import lru_cache
@lru_cache(maxsize=2)
def add(a, b):
    print('add called...')
    return a+b

print(add(1,2))
print(add(3,4))
print(add(1,2))
print(add(3,4))
print(add(5,6))
print(add(3,4))
print(add(1,2))
print('-'*80)

def fib(n):
    print(f'fib({n}) called...')
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(5))
print()

print(fib(8))
print()

print(fib(20))
print()
print('='*80)
