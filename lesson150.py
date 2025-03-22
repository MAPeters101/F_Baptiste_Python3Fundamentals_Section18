def wrapper(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return inner

def add(a, b, c):
    return a+b+c

def greet(name):
    return f'Hello {name}!'

def join(data, *, item_sep=',', line_sep='\n'):
    return line_sep.join(
        [
            item_sep.join(str(item) for item in row)
            for row in data
        ]
    )

print(add(1, 2, 3))
print(greet('Python'))
print(join([[1,2,3],[4,5,6],[7,8,9]]))
print('-'*80)

add_wrapped = wrapper(add)
greet_wrapped = wrapper(greet)
join_wrapped = wrapper(join)

print(add_wrapped(1,2,3))
print(greet_wrapped('Python'))
print(join_wrapped([[1,2,3],[4,5,6],[7,8,9]]))
print('-'*80)

def log(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__} called... result={result}')
        return result
    return inner

add_logged = log(add)
greet_logged = log(greet)
join_logged = log(join)

print(add_logged(1,2,3))
print(greet_logged('Python'))
print('-'*80)

print(hex(id(add)))
add = log(add)
print(hex(id(add)))
print(add.__closure__)
print('-'*80)

def add(a, b, c):
    return a+b+c
add = log(add)

def greet(name):
    return f'Hello {name}!'
greet = log(greet)

def join(data, *, item_sep=',', line_sep='\n'):
    return line_sep.join(
        [
            item_sep.join(str(item) for item in row)
            for row in data
        ]
    )
join = log(join)

print(greet('Python'))
print('-'*80)

@log
def add(a, b, c):
    return a+b+c
print(add(1,2,3))
print('-'*80)

import logging
logging.basicConfig(
    format='%(asctime)s %(levelname)s: %(message)s',
    level=logging.DEBUG
)
logger = logging.getLogger('Custom Log')
logger.debug('debug message')
logger.error('some error happened')
logger.warning('warning message')
print('='*80)
print()

from time import perf_counter

def log(func):
    def inner(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        logger.debug(f'called={func.__name__}, elapsed={end - start}')
        return result
    return inner

@log
def add(a,b,c):
    return a+b+c

@log
def greet(name):
    return f'Hello {name}!'

@log
def join(data, *, item_sep=',', line_sep='\n'):
    return line_sep.join([item_sep.join(str(item) for item in row) for row in data])

result = add(1,2,3)
print(result)
print('-'*80)





