
def yield_generator(max_number: int) -> None :
    for n in range(2, max_number+1) :
        for i in range(2, n) :
            if n % i == 0 :
                break
        else :
            yield n


if __name__ == '__main__' :

    max_num = int(input('max number : '))

    for i in yield_generator(max_num) :
        print(i)
