from typing import Any


def trace(func: Any) -> Any :
    def wrapper(*args, **kwargs) -> Any :
        r = func(*args, **kwargs)
        print('{0}(args={1}, kwargs={2})->{3}'.format(func.__name__, args, kwargs, r))

        return r
    return wrapper

@trace
def get_max(*args) -> Any:
    return max(args)

@trace
def get_min(**kwargs) -> Any:
    return min(kwargs.values())

@trace
def add(a: Any, b: Any) -> Any:
    return a + b

print(get_max(10, 20))
print(get_min(x=10, y=20, z=30))
print(add(10, 20))
print(add('Hello, ', 'world'))
