from typing import Any

def trace(func: Any) -> Any :
    def wrapper(a: Any, b: Any) -> Any:
        r = func(a, b)
        print('{0}(a={1}, b={2}) -> {3}'.format(func.__name__, a, b, r))
        return r
    return wrapper


@trace
def add(a: Any, b: Any) -> Any :
    return a + b

print(add(10, 20))
print(add('Hello', ' world'))

