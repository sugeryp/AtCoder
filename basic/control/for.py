some_list = [1, 2, 3, 4, 5]

i = 0
while i < len(some_list):
    print(some_list[i])
    i += 1

for i in some_list:
    print(i)

for s in 'abcde':
    print(s)

for word in ['My', 'name', 'is', 'Mike']:
    if word == 'is':
        continue
    print(word)

print('#########################################')
for fruit in ['apple', 'banana', 'orange']:
    if fruit == 'banana':
        print('skip eating')
    print(fruit)
else:
    print("I've finished eating")

print('#########################################')
num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in num_list:
    print(i)

print('#########################################')
for i in range(10):
    print(i)

print('#########################################')
for i in range(2, 10):
    print(i)

print('#########################################')
for i in range(2, 10, 3):
    print(i)

print('#########################################')
for _ in range(10):
    print('hello')

print('#########################################')
i = 0
for fruit in ['apple', 'banana', 'orange']:
    print(i, fruit)    
    i += 1

print('#########################################')
for i, fruit in enumerate(['appale', 'banana', 'orange']):
    print(i, fruit)

print('#########################################')
days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['cofee', 'tea', 'beer']

for i in range(len(days)):
    print(days[i], fruits[i], drinks[i])

print('#########################################')
days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['cofee', 'tea', 'beer']

for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)

print('#########################################')
d = {'x': 100, 'y': 200}

for v in d:
    print(v)

print('#########################################')
d = {'x': 100, 'y': 200}
for k, v in d.items():
    print(k, ':', v)

print('#########################################')
print(d.items())