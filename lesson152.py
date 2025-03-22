
def cache(func):
    def inner(*args):
        result = func(*args)
        return result
    return inner





