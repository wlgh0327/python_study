class NotThreeMultipleError(Exception) :
    def __init__(self) :
        super().__init__("Not 3's multiplier")


def three_multiple():
    try :
        x = int(input('input a number : '))
        if x % 3 != 0 :
            raise NotThreeMultipleError

        print(x)

    except Exception as e :
        print(e)

if __name__ == '__main__' :
    three_multiple()
