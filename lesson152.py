
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




