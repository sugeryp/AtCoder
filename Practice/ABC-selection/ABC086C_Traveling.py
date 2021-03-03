n = int(input())
plans = [tuple(map(int, input().split())) for _ in range(n)]

t, px, py = 0, 0, 0

for plan in plans:
    dt = plan[0] - t
    x = plan[1]
    y = plan[2]
    for _ in range(dt):
        if x > px:
            px += 1
        elif x < px:
            px -= 1
        elif y > py:
            py += 1
        elif y < py:
            py -= 1
        else:
            px += 1
        t += 1
    if x == px and y == py:
        continue
    print('No')
    break
else:
    print('Yes')

"""
t = dist 折り返し無しの場合
dist = t - 2x 折り返しありの場合

押し返し無しの場合
dist = t となりdistが最大
  dist = t

折り返しがある場合
dist = t - 2xとなりdistはt以下
また、t + dist = 2t -2xとなりt + distは偶数
  dist < t
  t + dist % 2 == 0


dist = t or
(dist < t and t + dist % 2 == 0)
  yes

dist != t and
dist > t or t + dist % 2 == 1
  no

dist > tのときdist != tなので
if dist > t or t + dist % 2 == 1
  no
else
  yae

"""


# from sys import stdin
# input = stdin.buffer.readline
 
# def main():
#     n = int(input()) 
#     t, x, y = 0, 0, 0
#     for i in range(1, n+1):
#         new_t, new_x, new_y = map(int, input().split())
#         time = new_t - t
#         dist = abs(new_x - x) + abs(new_y - y)
 
#         if time < dist or (time + dist) % 2 == 1:
#             print('No')
#             exit()
            
#         t, x, y = new_t, new_x, new_y
 
#     print('Yes')
 
# main()
