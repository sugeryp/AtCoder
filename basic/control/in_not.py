print('list')
y = [1, 2, 3]
x = 1

if x in y:
    print('in')

if 100 not in y:
    print('not in')

print('tuple')
y = (1, 2, 3)
x = 1

if x in y:
    print('in')

if 100 not in y:
    print('not in')

print('set')
y = {1, 2, 3}
x = 1

if x in y:
    print('in')

if 100 not in y:
    print('not in')

print('dictionaly')
y = {1: 100, 2: 200, 3: 300}
x = 1

if x in y:
    print('in')

if 100 not in y:
    print('not in')


print('############################################')

# a = 1
# b = 2

# if not a == b:
#     print('not equal')

# if not a <= b:
#     print('not less or equal then greater')

# if a > b:
#     print('not less or equal then greater')

is_ok = True
if not is_ok:
    print('not hello')
if is_ok:
    print('hello')

is_ok = 100
if is_ok:
    print('true')

is_ok = []
if not is_ok:
    print('false')

is_ok = [1, 2]
if is_ok:
    print('true')