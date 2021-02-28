def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper


def add_num(a, b):
    return a + b


f = print_info(add_num)
r = f(10, 20)
print(r)

print('############################################')


# decorator
def print_info2(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper


@print_info2
def add_num2(a, b):
    return a + b


r = add_num2(10, 20)
print(r)

print('############################################')


# decorator
def print_more(func):
    def wrapper(*args, **kwargs):
        print('func', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper


def print_info3(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper


@print_info3
@print_more
def add_num3(a, b):
    return a + b


r = add_num3(10, 20)
print(r)
