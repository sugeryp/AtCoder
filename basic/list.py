l = [1, 20, 4, 50, 2, 1, 2]
l = [1, 20, 4, 50, 2, 1, 2]
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = ['a', 'b', 'c']
b = [1, 2, 3]
c = [a, b]

print(f"""\
{l[1]}
{l[-1]}
{l[-2]}
{l[0:2]}
{l[:2]}
{l[2:5]}
{l[2:]}
{l[:]}
{len(l)}
{list('abcdefg')}

{n}
{n[::2]}
{n[::-1]}
{n[::-2]}

{c}
{c[0]}
{c[0][1]}
\
""")
print('###################################################')

print('###################################################')
s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

print(s[0])
s[0] = 'X'
print(s[0])
s[2:5] = ['C', 'D', 'E']
print(s)
s[2:5] = []
print(s)
s[:] = []
print(s)
print(n)
n.append(100)
print(n)
n.insert(0, 200)
print(n)
n.pop(0)
print(n)
del n[0]
print(n)
if 'n' in globals():
    print('exist s beyond')
del n
if 'n' in globals():
    print('exist s after')

n = [1, 2, 2, 2, 3]
n.remove(2)
print(n)
n.remove(2)
n.remove(2)
print(n)

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

a += b
print(a)

del a[5:]
print(a)

a.extend(b)
print(a)

print('###################################################')

r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3))
print(r.index(3, 3))

print(r.count(3))

if 5 in r:
    print('exist')

print(r)
r.sort()
print(r)

r.reverse()
print(r)

r.sort(reverse=True)
print(r)

r.reverse()
print(r)

s = 'My name is Mike'
to_split = s.split(' ')
print(to_split)

to_split2 = s.split('lerfketke')
print(to_split2)

to_join = ' '.join(to_split)
print(to_join)
to_join = '####'.join(to_split)
print(to_join)
# print(help(list))

i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print('j =', j)
print('i =', i)
print(id(i))
print(id(j))

x = [1, 2, 3, 4, 5]
y = x.copy()
x[0] = 100
print('x=', x)
print('y=', y)
print(id(x))
print(id(y))

x = [1, 2, 3, 4, 5, 6]
y = x[:]
x[0] = 100
print('x=', x)
print('y=', y)

# sample taxi