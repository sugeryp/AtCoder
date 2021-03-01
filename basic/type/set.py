a = {1, 2, 3, 4, 4, 4, 5, 6}
b = {2, 3, 3, 6, 7}

print(a)
print(b)
print(type(a), type(b))

print(a - b)
print(b - a)
print(a & b)
print(a | b)
print(b ^ a)

print(a.add(8))
print(a)
print(a.add(8))
print(a)
print(a.remove(8))
print(a)
print(a.clear())
print(a)

# sample
my_friend = {'A', 'B', 'C'}
A_friend = {'B', 'C', 'D'}

print(my_friend & A_friend)


f = ['apple', 'banana', 'apple']
kind = set(f)
print(kind)
