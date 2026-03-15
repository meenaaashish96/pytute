#cache system 
import time
def cache(func):
    cache_val = {}
    def wrapper(*args):
        if args in cache_val:
            return cache_val[args]
        result = func(args)
        cache_val[args] = result
        return result
    return wrapper
@cache
def hello(greet):
    time.sleep(2)
    print(f"{greet}")

hello("Kristen")
hello("Kristen")