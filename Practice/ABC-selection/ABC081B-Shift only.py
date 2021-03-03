# total-number input
total_number = int(input())

# integers input
integers = list(map(int, input().split()))

# Even-number judgment
count = 0
while sum(i % 2 for i in integers) == 0:
    integers = [i / 2 for i in integers]
    count += 1

# count output
print(count)