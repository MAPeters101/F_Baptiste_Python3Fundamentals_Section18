def wrapper(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return inner


