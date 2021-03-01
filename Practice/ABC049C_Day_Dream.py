# s = input()


# def day_dream(t_list):
#     t_list_add = []
#     for t in t_list:
#         t_list_add.append(t + 'dream')
#         t_list_add.append(t + 'dreamer')
#         t_list_add.append(t + 'erase')
#         t_list_add.append(t + 'eraser')
#     return t_list_add


# def check(t_list, count, fn):
#     for t in t_list:
#         if t == s:
#             print('YES')
#             count += 1
#             break
#         elif len(t) >= len(s):
#             print('NO')
#             count += 1
#             break
#         else:
#             return fn(t_list)


# t_list = day_dream([''])
# count = 0

# while count == 0:
#     check(t_list, count, day_dream)

s = input()
while len(s) > 0:
    if s.endswith('dreamer'):
        s = s[:-7]
    elif s.endswith('dream'):
        s = s[:-5]
    elif s.endswith('eraser'):
        s = s[:-6]
    elif s.endswith('erase'):
        s = s[:-5]
    else:
        print('NO')
        break
else:
    print('YES')
