
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

print(add.__closure__)
print(mult.__closure__)





