from typing import Any

def trace(func: Any) -> Any:
    def wrapper(self, a: Any, b: Any) -> Any:
        r = func(self, a, b)
        print('{0}(a={1}, b={2}) -> {3}'.format(func.__name__, a, b, r))
        return r

    return wrapper

class Calc:
    @trace
    def add(self, a: Any, b: Any) -> Any :
        return a + b

if __name__ == '__main__' :
    c = Calc()
    print(c.add(10, 20))
    print(c.add('Hello, ', 'world'))
