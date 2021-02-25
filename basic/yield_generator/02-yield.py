def number_generator(stop) :
    n = 0
    while n < stop :
        yield n
        n = n + 1



for i in number_generator(3) :
    print(i)


def upper_generator(l) :
    for dat in l :
        yield dat.upper()

fruits = ['apple', 'banana']

for i in upper_generator(fruits) :
    print(i)


def three_generator() :
    yield from number_generator(3)



for i in three_generator() :
    print(i)

