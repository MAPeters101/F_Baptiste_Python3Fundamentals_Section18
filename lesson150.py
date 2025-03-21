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





