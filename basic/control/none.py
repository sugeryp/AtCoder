# null is none object in python

is_empty = None
# print(help(is_empty))

# if is_empty == None:
#     print('None!')

if is_empty is None:
    print('None!')

if is_empty is not None:
    print('not None')

print(1 == True)   # True
print(1 is True)   # False
print([] == True)   # False
print([] is True)   # False
print(0 == False)   # True
print(0 is False)   # False
print([] == False)   # False


def test(a=None):
    print(a)


if test() is None:
    print('None!!!')
else:
    print('not None!')
