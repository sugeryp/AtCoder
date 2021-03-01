n, a, b = input().split()
a = int(a)
b = int(b)

some_sums = 0
for some in range(int(n) + 1):
    some_list = list(str(some))
    i_sum = 0
    for i in some_list:
        i_sum += int(i)
    if a <= i_sum and i_sum <= b:
        some_sums += some

print(some_sums)
