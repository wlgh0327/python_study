from typing import Any

class Counter :
    def __init__(self, stop: int) -> None :
        self.current = 0
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop:
            r = self.current
            self.current += 1
            return r
        else :
            raise StopIteration


    def __getitem__(self, index) :
        if index < self.stop:
            return index
        else :
            raise IndexError


for i in Counter(3):
    print(i, end=' ')
print()

print(Counter(3)[0], Counter(3)[1], Counter(3)[2])

