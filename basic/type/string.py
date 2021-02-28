print('###################################################')
print("""
line1
line2
line3
""")
print('###################################################')


print("""\
line1
line2
line3\
""")
print('###################################################')


s = ('aaaaaaaaaaaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbbbbbbbbbbb')
print(s)

s2 = ('aaaaaaaaaaaaaaaaaaaaaaaaaaa\n'
      "bbbbbbbbbbbbb'bbbb\"bbbbbbbbbb")

path = ('C:\name\name')
path2 = (r'C:\name\name')

print(path)
print(path2)
print('\nslice##############################################')


word = 'python'
print(word[0])
print(word[1])
print(word[-1])
print(word[0:2])
print(word[2:5])
print(word[0:2])
print(word[:2])
print(word[2:])
word = 'j' + word[1:]
print(word)
print(word[:])
n = len(word)
print(n)
print('###################################################')


s = 'My name is Mike. Hi Mike'
print(s)
is_start = s.startswith('My')
print(is_start)
is_start = s.startswith('Mike')
print(is_start)

# 前のMike
print(s.find('Mike'))
# 後ろのMike
print(s.rfind('Mike'))

print(s.count('Mike'))
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('Mike', 'Nancy'))
print('format#################################################')

print('My name is {} {}'.format('Akihiro', 'Kondo'))
print('My name is {0} {1}'.format('Akihiro', 'Kondo'))
print('My name is {1} {0}'.format('Akihiro', 'Kondo'))
print('My name is {name} {family}'.format(name='Akihiro', family='Kondo'))
print('{} {} {}'.format(1, 2, 3))
print(str(1))


li = [1, 20, 4, 50, 2, 1, 2]
li = [1, 20, 4, 50, 2, 1, 2]

print(f"""\
{li[1]}
{li[-1]}\
""")
