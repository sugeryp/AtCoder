n = int(input())
card_list = list(map(int, input().split()))

card_list.sort(reverse=True)

# alice_cards = []
# bob_cards = []
# for card in card_list:
#     if len(alice_cards) <= len(bob_cards):
#         alice_cards.append(card)
#     else:
#         bob_cards.append(card)

# print(sum(alice_cards) - sum(bob_cards))

alice_sum = 0
bob_sum = 0

for i in range(n):
    if i % 2 == 0:
        alice_sum += card_list[i]
    else:
        bob_sum += card_list[i]

print(alice_sum - bob_sum)
