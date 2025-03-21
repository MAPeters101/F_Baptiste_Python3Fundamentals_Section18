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

