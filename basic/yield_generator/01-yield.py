def generator() :
    yield 0
    yield 1
    yield 2


for i in generator() :
    print(i)

for i in generator():
    print(i)

g = generator()

print(g)

print(dir(g))

