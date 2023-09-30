# invert values
numbers = input().split()
opposite_numbers = []
for number in numbers:
    current_number = -int(number)
    opposite_numbers.append(current_number)
print(opposite_numbers)

# print([-int(number) for number in input().split()])

# multiples list
factor = int(input())
count = int(input())
list_of_numbers = []
for multiplier in range(1, count+1):
    list_of_numbers.append(factor*multiplier)
print(list_of_numbers)

# football cards
team_a = ["A-" + str(s) for s in range(1, 12)]
team_b = ["B-" + str(s) for s in range(1, 12)]
players = input().split()
game_termination = False
for player in players:
    if player in team_a:
        team_a.remove(player)
    elif player in team_b:
        team_b.remove(player)
    if len(team_a) < 7 or len(team_b) < 7:
        game_termination = True
        break
print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if game_termination:
    print("Game was terminated")

# number beggars
money_string = input().split(", ")
count_of_beggars = int(input())
money = []
for current_money in money_string:
    money.append(int(current_money))
final_sums = []
start_index = 0
while start_index < count_of_beggars:
    current_beggar_sum = 0
    for current_index in range(start_index, len(money), count_of_beggars):
        current_beggar_sum += money[current_index]
    final_sums.append(current_beggar_sum)
    start_index += 1
print(final_sums)

# faro shuffle
deck_of_cards = input().split()
count_of_shuffles = int(input())
for shuffle in range(count_of_shuffles):
    middle = len(deck_of_cards) // 2
    left_part = deck_of_cards[0:middle]
    right_part = deck_of_cards[middle:]
    deck_after_shuffle = []
    for card in range(len(left_part)):
        deck_after_shuffle.append(left_part[card])
        deck_after_shuffle.append(right_part[card])
    deck_of_cards = deck_after_shuffle
print(deck_of_cards)

# survival of the biggest


# bread factory



