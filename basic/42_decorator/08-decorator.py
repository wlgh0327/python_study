
def type_check(type_a, type_b) :
    def real_decorator(func) :
        def wrapper(a, b) :
            if isinstance(a, type_a) and isinstance(b, type_b) :
                return func(a, b)
            else :
                raise RuntimeError('Invalid data type')

        return wrapper
    return real_decorator

@type_check(int, int)
def add(a, b):
    return a + b

print(add(10, 20))
print(add('hello', 'world'))
