from typing import Any

def trace(func: Any) -> Any :
    def wrapper() -> None:
        print(func.__name__, 'func started')
        func()
        print(func.__name__, 'func ended')

    return wrapper

@trace
def hello() -> None:
    print('hello')

@trace
def world() -> None:
    print('world')


if __name__ == '__main__' :

    hello()
    world()


