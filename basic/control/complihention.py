t = (1, 2, 3, 4, 5)
t2 = (5, 6, 7, 8, 9, 10)

r = []
for i in t:
    for j in t2:
        r.append(i * j)

print(r)

r = [i * j for i in t for j in t2]
print(r)

print('###############################################')
# dictionary complehention
w = ['mon', 'tue', 'wed']
f = ['cofee', 'milk', 'water']

d = {}
for x, y in zip(w, f):
    d[x] = y

print(d)

d = {x: y for x, y in zip(w, f)}
print(d)

print("##################################################")
# set complehention
s = set()

for i in range(10):
    if i % 2 == 0:
        s.add(i)

print(s)

s = {i for i in range(10) if i % 2 == 0}
print(s)

print("##################################################")
# generator complehention


def g():
    for i in range(10):
        if i % 2 == 0:
            yield i


g = g()

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

print("##################################################")
# generator complehention

g = (i for i in range(10) if i % 2 == 0)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

print(type(g))
print(g)

print("##################################################")
# tuple complehention

g = tuple(i for i in range(10))
print(g)
