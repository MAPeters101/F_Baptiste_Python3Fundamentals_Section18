def wrapper(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return inner

def add(a, b, c):
    return a+b+c

def greet(name):
    return f'Hello {name}'

def join(data, *, item_sep=',', line_sep='\n'):
    return line_sep.join(
        [
            item_sep.join(str(item) for item in row)
            for row in data
        ]
    )
