d = {'x': 10, 'y': 20}
print(type(d))
print(d['x'])

d['x'] = 100
print(d)

d['x'] = 'xxxxxxxxxxxx'
print(d)

d['z'] = 200
print(d)

d[1] = 1000
print(d)

print(dict(a=10, b=20))
print(dict([('a', 10), ('b', 20)]))

print('method##################################################')

print(d)
print(d.keys())
print(d.values())

d2 = {'x': 'pekepon', 'a': 999}
print(d.update(d2))
print(d)

print(d.get('x'))
print(d)
print(d.pop('x'))
print(d)
del d['y']

print('z' in d)
print('x' in d)

print(d.clear())
print(d)

if 'd' in locals():
    print('exist')

del d

if 'd' not in locals():
    print('not exist')

d = {'x': 10, 'y': 20}
d2 = d
d2['x'] = 100
print(d2)
print(d)

d = {'x': 10, 'y': 20}
d2 = d.copy()
d2['x'] = 100
print(d2)
print(d)


# sample
# item: value
# dictionaly uses hashtable then to search value fastly than list 