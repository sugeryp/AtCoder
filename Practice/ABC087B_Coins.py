# coins-number input
gohyakuen_number = int(input())
hyakuen_number = int(input())
gozyuen_number = int(input())
total_amount = int(input())

# combination count
# count gohyakuen
# count hyakuen
# count gozyuen

count = 0
for sum_gohyakuen in range(gohyakuen_number):
    tmp1 = total_amount
    tmp1 -= 500 * sum_gohyakuen
    if tmp1 < 0 or gohyakuen_number - sum_gohyakuen < 0:
        break
    for sum_hyakuen in range(hyakuen_number):
        tmp2 = tmp1
        tmp2 -= 100 * sum_hyakuen
        if tmp2 < 0 or hyakuen_number - sum_hyakuen < 0:
            break
        for sum_gozyuen in range(gozyuen_number):
            tmp3 = tmp2
            tmp3 -= 50 * sum_gozyuen
            if tmp3 == 0:
                count += 1
                break
            elif tmp3 < 0:
                break

print(count)


a
            
        