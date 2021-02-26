def number_coroutine():
    while True :
        x = (yield)
        print(x)

co = number_coroutine()
next(co)

co.send(1)
co.send(2)
co.send(3)
