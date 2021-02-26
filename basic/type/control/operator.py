a = 1
b = 2

if a == b:
    print('equal')

if a != b:
    print('not equal')

if a < b:
    print('a is less than b')

if a > b:
    print('a is greater than b')

if a <= b:
    print('a is less than or equal to b')

if a >= b:
    print('a is greater than or equal to b')

if a > 0 and b > 0:
    print('a and b are positive')

if a > 0 or b > 0:
    print('a or b is positive')

if a > 0:
    if b > 0:
        print('a and b are positive')

if a > 0:
    print('a or b is positive')
elif b > 0:
    print('a or b is positive')