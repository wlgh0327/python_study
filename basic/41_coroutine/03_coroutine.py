def number_coroutine() :
    try :
        while True:
            x = (yield)
            print(x, end=' ')
    except GeneratorExit:
        print()
        print('Exit coroutine')



co = number_coroutine()
next(co)

for i in range(20) :
    co.send(i)

co.close()

def sum_coroutine():
    try :
        total = 0
        while True :
            x = (yield)
            total += x
    except RuntimeError as e :
        print(e)
        yield total


co = sum_coroutine()
next(co)

for i in range(20) :
    co.send(i)

print(co.throw(RuntimeError, 'Terminate the coroutine with throw exception'))
