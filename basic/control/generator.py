li = ['Good mornin', 'Good afternoon', 'Good night']

for i in li:
    print(i)

print('##########################')


def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'


for g in greeting():
    print(g)

print('##########################')
print(greeting())

print('##########################')

g = greeting()
print(next(g))

print('@@@@@@@')
print(next(g))

print('@@@@@@@')
print(next(g))
print('##########################')


def counter(num=10):
    for _ in range(num):
        yield 'run'


def greeting2():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'


g = greeting2()
c = counter()

print(next(g))

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))
print('##########################')


def counter2(num=10):
    for _ in range(num):
        yield 'run'


def greeting3():
    yield 'Good morning'
    for _ in range(10000):
        print('push up')
    yield 'Good afternoon'
    for _ in range(20000):
        print('squad')
    yield 'Good night'


g = greeting3()
c = counter2()

print(next(g))
print(next(c))
print(next(c))
print(next(g))
print(next(c))
print(next(c))
print(next(g))
