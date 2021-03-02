from typing import Any


def try_test() -> None :
    try:
        x = int(input('input a number : '))
        y = 10 / x
        print(y)
    except :
        print('Except')


def try_test2() -> None :
    y = [10, 20, 30]

    try :
        index, x = map(int, input('index & number : ').split())
        print(y[index] / x)
    except ZeroDivisionError as e:
        print('zero division error', e)
    except IndexError as e :
        print('Index Error', e)



if __name__ == '__main__' :

    try_test2()
