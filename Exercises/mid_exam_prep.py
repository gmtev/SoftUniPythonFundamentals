# black flag
days = int(input())
daily_plunder = int(input())
daily_third = daily_plunder * 1.5
expected_plunder = float(input())
plunder = 0
for day in range(1, days+1):
    if day % 3 == 0:
        plunder += daily_third
    else:
        plunder += daily_plunder
    if day % 5 == 0:
        plunder -= plunder * 0.3
if float(plunder) >= expected_plunder:
    print(f"Ahoy! {plunder:.2f} plunder gained.")
else:
    print(f"Collected only {(float(plunder)/expected_plunder)*100:.2f}% of the plunder.")

# shopping list
shopping_list = input().split("!")
command = input().split()
while command[0] != "Go":
    if command[0] == "Urgent":
        if command[1] not in shopping_list:
            shopping_list.insert(0, command[1])
    elif command[0] == "Unnecessary":
        if command[1] in shopping_list:
            shopping_list.remove(command[1])
    elif command[0] == "Correct":
        shopping_list = [command[2] if checker == command[1] else checker for checker in shopping_list]
    elif command[0] == "Rearrange":
        if command[1] in shopping_list:
            shopping_list.remove(command[1])
            shopping_list.append(command[1])
    command = input().split()
print(', '.join(shopping_list))

# memory game
elements = input().split()
game_command = input().split()
moves = 0
while game_command[0] != "end":
    if not elements:
        break
    moves += 1
    index1, index2 = int(game_command[0]), int(game_command[1])
    if index1 == index2 or index1 < 0 or index2 < 0\
            or index1 > len(elements)-1 \
            or index2 > len(elements)-1:
        print("Invalid input! Adding additional elements to the board")
        midpoint = len(elements) // 2
        new_elements = 2 * [f"-{moves}a"]
        elements = elements[0:midpoint] + new_elements + elements[midpoint:]
    elif elements[index1] == elements[index2]:
        print(f"Congrats! You have found matching elements - {elements[int(index1)]}!")
        to_be_removed = [elements[index1], elements[index2]]
        elements = [remover for remover in elements if remover not in to_be_removed]
        to_be_removed.clear()
    else:
        print("Try again!")
    game_command = input().split()
if elements:
    print(f"Sorry you lose :(\n{' '.join(elements)}")
else:
    print(f"You have won in {moves} turns!")


