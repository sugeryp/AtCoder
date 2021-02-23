def calcurate(a, b, c):
    result = a + b + c
    return result

a = int(input())
b, c = map(int, input().split())
s = input()

print("{} {}".format(calcurate(a, b, c), s))