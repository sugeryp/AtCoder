n, otoshidama = list(map(int, input().split()))

for x in range(n + 1):
    for y in range(n + 1 - x):
        z = n - x - y
        if 10000*x + 5000*y + 1000*z == otoshidama:
            print('{} {} {}'.format(x, y, z))
            break
    else:
        continue
    break
else:
    print('-1 -1 -1')
