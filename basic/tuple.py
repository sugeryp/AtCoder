t = (1, 2, 3)
print(t)
print(type(t))

t = 1,
print(t)
print(type(t))

t = (1)
print(t)
print(type(t))

t = ()
print(type(t))

t = 1, 2
print(t)
print(type(t))

t = (1, 2, 3, 4, 5, 6, 4)
print(t[:3])
print(t[2:3])
print(t.index(5))
print(t.count(4))

t = ([1, 2, 3], [4, 5, 6])
print(t)
t[0][2] = 100
print(t)

new_tuple = (1, 2, 3) + (4, 5) + (6,)
print(new_tuple)