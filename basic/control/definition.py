def say_something():
    print('hi')

say_something()
print(type(say_something))

print('############################################')
def say_something2():
    print('hihi')

f = say_something2
f()

print('############################################')
def say_something3():
    s = 'hihihi'
    return s

result = say_something3()
print(result)

print('############################################')
def what_is_this(color):
    print(color)

what_is_this('red')

print('############################################')
def what_is_this2(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"

result = what_is_this2('red')
print(result)
result = what_is_this2('green')
print(result)
result = what_is_this2('yellow')
print(result)

print('############################################')
num: int = 10
print(num)

print('############################################')
def add_num(a: int, b: int) -> int:
    return a + b

r = add_num('a', 'b')
print(r)

print('############################################')
def menu(entree, drink, dessert):
    print(entree)
    print(drink)
    print(dessert)

menu(entree='beef', dessert='ice', drink='beer')

print('############################################')
def menu2(entree='beef', drink='beer', dessert='ice'):
    print(entree)
    print(drink)
    print(dessert)
    
menu2(drink='wine')

print('############################################')
# wrong example with empty list
def test_func(x, l=[]):
    l.append(x)
    return l

r = test_func(100)
print(r)

r = test_func(200)
print(r)

y = [1, 2, 3]
r = test_func(100, y)
print(r)

y = [1, 2, 3]
r = test_func(200, y)
print(r)

print('############################################')
# right example with empty list
def test_func2(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l

r = test_func2(100)
print(r)

r = test_func2(200)
print(r)

print('############################################')
def say_something4(*args):
    print(args)
    for arg in args:
        print(arg)

say_something4('Hi!', 'Mike', 'Nancy')

print('############################################')
def say_something5(word, *args):
    print('word=', word)
    for arg in args:
        print(arg)

say_something5('Hi!', 'Mike', 'Nancy')

print('############################################')
def say_something6(word, *args):
    print('word=', word)
    for arg in args:
        print(arg)

t = ('Mike', 'Nancy')
say_something6('Hi!', *t)

print('############################################')
def menu3(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)

menu3(entree='beef', drink='cofee')

print('############################################')
def menu4(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

d = {
    'entree': 'beef',
    'drink': 'ice cofee',
    'dessert': 'ice'
}

menu4(**d)

print('############################################')
def menu5(visit_time, *args, **kwargs):
    print(visit_time)
    for k in args:
        print(k)
        for i, j in kwargs.items():
            print(i, j)

t = ('Json', 'Katy')

d = {
    'entree': 'beef',
    'drink': 'ice cofee',
    'dessert': 'ice'
}

menu5('12', *t, **d)

print('############################################')
def example_func(param1, param2):
    """Example function with types documented in the docstring.

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter. 

    Returns:
        bool: The return value. True for success, False 
    """
    print(param1)
    print(param2)
    return True

print(example_func.__doc__)
# help(example_function) only available in intaractively

print('############################################')
def outer(a, b):

    def plus(c, d):
        return c + d
    
    r1 = plus(a, b)
    r2 = plus(b, a)
    print(r1 + r2)

outer(1, 2)

print('############################################')
# closure
def outer2(a, b):

    def inner():
        return a + b
    
    return inner

print(outer2(1, 2))
f = outer2(1, 2)
r = f()
print(r)

print('############################################')
# closure sample
def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius
    
    return circle_area

ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.141592)

print(ca1(10))
print(ca2(10))

print('############################################')
# decorator

def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

def add_num2(a, b):
    return a + b

f = print_info(add_num2)
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
def add_num3(a, b):
    return a + b

r = add_num3(10, 20)
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
def add_num4(a, b):
    return a + b

r = add_num4(10, 20)
print(r)