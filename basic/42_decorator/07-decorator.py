from typing import Any
import functools

class Trace:
    def __init__(self, func: Any) -> None :
        self.func = func

    def __call__(self) -> Any:
        print(self.func.__name__, 'function start')
        self.func()
        print(self.func.__name__, 'function end')


class Trace2:
    def __init__(self, func: Any) -> None :
        self.func = func

    def __call__(self, *args, **kwargs) -> Any:
        r = self.func(*args, **kwargs)
        print('{0}(args={1}, kwargs={2}) -> {3}'.format(self.func.__name__, args, kwargs, r))
        return r


class IsMultiple :
    def __init__(self, x: int) -> None :
        self.x = x

    def __call__(self, func: Any) -> Any :
        def wrapper(a: int, b: int) -> int :
            r = func(a, b)
            if r % self.x == 0 :
                print("{0}'s return value is {1} multiplied".format(func.__name__, self.x))
            else :
                print("{0}'s return value is not {1} multiplied".format(func.__name__, self.x))

            return r
        return wrapper

                
@Trace
def hello():
    print('hello')


@Trace2
def add(a: Any, b: Any) -> Any :
    return a+b

@IsMultiple(3)
def mul(a: int, b: int) -> int :
    return a * b


if __name__ == '__main__' :
    hello()
    print(add(10, 20))
    print(add(a=10, b=20))
    print(add('hello, ', 'world'))

    print(mul(10, 20))
    print(mul(2, 5))

