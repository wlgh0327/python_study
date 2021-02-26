from typing import Any

def trace(func: Any) -> Any :
    def wrapper() -> None:
        print(func.__name__, 'func started')
        func()
        print(func.__name__, 'func ended')

    return wrapper

def hello() -> None:
    print('hello')

def world() -> None:
    print('world')


if __name__ == '__main__' :

    trace_hello = trace(hello)
    trace_hello()
    trace_world = trace(world)
    trace_world()


