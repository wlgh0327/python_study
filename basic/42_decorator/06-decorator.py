from typing import Any
import functools


def is_multiple(x: int) -> Any:
    def real_decorator(func: Any) -> Any:
        @functools.wraps(func)
        def wrapper(a: int, b: int) -> int:
            r = func(a, b)
            if r % x == 0:
                print('{0} value is {1} multiplied'.format(func.__name__, x))
            else :
                print('{0} value is {1} not multiplied'.format(func.__name__, x))

            return r
        return wrapper
    return real_decorator


@is_multiple(3)
@is_multiple(7)
def add(a, b) :
    return a + b

print(add(10, 20))
print(add(2, 5))

