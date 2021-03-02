from typing import Any

class MultipleIterator :
    def __init__(self, stop: int, multiple: int) -> None :
        self.stop = stop
        self.multiple = multiple
        self.current = multiple 

    def __iter__(self) :
        return self

    def __next__(self) :
        if self.current < self.stop :
            r = self.current
            self.current += self.multiple
            return r

        else :
            raise StopIteration

    def __getitem__(self, index) :
        if index < self.stop:
            return index
        else :
            raise IndexError


if __name__ == '__main__' :

    for i in MultipleIterator(20, 3) :
        print(i, end= ' ')

    print()

    for i in MultipleIterator(30, 5) :
        print(i, end = ' ')

    print()

