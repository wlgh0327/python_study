from typing import Any

def try_test() -> None :
    try :
        x = int(input('input a number : '))
        y = 10 / x

    except ZeroDivisionError as e :
        print(e)

    else :
        print(y)
    
    finally :
        print('Done')

def try_test2() -> None :
    try :
        x = int(input('input a number : '))
        if x % 3 != 0 :
            raise Exception('Error!')
        print(x)
    except Exception as e :
        print(e)


def three_multiple()->None :
    x = int(input('input a number : '))
    if x % 3 != 0 :
        raise Exception('Error')
    print(x)


def three_multiple2() -> None :
    try :
        x = int(input('input a number : '))
        if x % 3 != 0 :
            raise Exception('Error')
        print(x)
    except Exception as e :
        print('error in three_multiple()', e)
        raise

if __name__ == '__main__' :
    try_test2()

    try :
        three_multiple2()
    except Exception as e :
        print(e)
