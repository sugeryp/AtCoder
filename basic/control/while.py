count = 0

while count < 5:
    print(count)
    count += 1

print('#################################')
count = 0

while True:
    print(count)
    if count >= 5:
        print('break')
        break
    count += 1

print('#################################')
count = 0

while count < 5:
    if count == 2:
        count += 1
        print('continue')
        continue

    print(count)
    count += 1

print('#################################')
count = 0

while count < 5:
    print(count)
    count += 1
else:
    print('done')

print('#################################')
count = 0
while count < 5:
    if count == 2:
        print('break')
        break
    print(count)
    count += 1
else:
    print('done')

print('#################################')

while True:
    word = input('Enter:')
    num = int(word)
    if num == 100:
        break
    print('next')