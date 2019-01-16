from functools import wraps

def wrapper(func):
    @wraps(func)
    def inner(*args,**kwargs):
       return func(*args,**kwargs)
    return inner



