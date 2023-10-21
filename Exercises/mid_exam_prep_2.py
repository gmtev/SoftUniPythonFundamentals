# bonus scoring system
from math import ceil
students = int(input())
lectures = int(input())
bonus = int(input())
current_highest = 0
most_attendances = 0
for i in range(students):
    attendances = int(input())
    total_bonus = attendances / lectures * (5 + bonus)
    if total_bonus > current_highest:
        current_highest = total_bonus
        most_attendances = attendances
print(f"Max Bonus: {ceil(current_highest)}.\nThe student has attended {most_attendances} lectures.")

# mu online
health = 100
bitcoin = 0
rooms = input().split("|")
counter = 0
for i in rooms:
    counter += 1
    command, amount = i.split(" ")
    if command == "potion":
        if health + int(amount) > 100:
            amount = abs(health - 100)
            health = 100
        else:
            health += int(amount)
        print(f"You healed for {amount} hp.\nCurrent health: {health} hp.")
    elif command == "chest":
        bitcoin += int(amount)
        print(f"You found {amount} bitcoins.")
    else:
        health -= int(amount)
        if health <= 0:
            print(f"You died! Killed by {command}.\nBest room: {counter}")
            break
        else:
            print(f"You slayed {command}.")
if health > 0:
    print(f"You've made it!\nBitcoins: {bitcoin}\nHealth: {health}")

# man-o-war
pirate_status = [int(i) for i in input().split(">")]
warship_status = [int(i) for i in input().split(">")]
health = int(input())
while True:
    command = input().split()
    if command[0] == "Retire":
        break
    elif command[0] == "Fire":
        if len(warship_status) > int(command[1]) >= 0:
            warship_status[int(command[1])] -= int(command[2])
            if warship_status[int(command[1])] <= 0:
                print(f"You won! The enemy ship has sunken.")
                exit()
    elif command[0] == "Defend":
        if 0 <= int(command[1]) < len(pirate_status) and 0 <= int(command[2]) < len(pirate_status)\
                and int(command[3]) > 0:
            for i in range(int(command[1]), int(command[2])+1):
                pirate_status[i] -= int(command[3])
                if pirate_status[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit()
    elif command[0] == "Repair":
        if 0 <= int(command[1]) < len(pirate_status) and int(command[2]) > 0:
            pirate_status[int(command[1])] += int(command[2])
            if pirate_status[int(command[1])] > health:
                pirate_status[int(command[1])] = health
    elif command[0] == "Status":
        to_be_repaired = [i for i in pirate_status if i < 0.2 * health]
        print(f"{len(to_be_repaired)} sections need repair.")
if pirate_status and warship_status:
    print(f"Pirate ship status: {sum(pirate_status)}\nWarship status: {sum(warship_status)}")

# with functions


def fire(warship, index, damage):
    warship[index] -= damage
    if warship[index] <= 0:
        print(f"You won! The enemy ship has sunken.")
        exit()


def defend(pirate_ship, starting, ending, damage):
    for i in range(starting, ending + 1):
        pirate_ship[i] -= damage
        if pirate_ship[i] <= 0:
            print("You lost! The pirate ship has sunken.")
            exit()


def repair(pirate_ship, index, healing):
    pirate_ship[index] += healing
    if pirate_status[index] > health:
        pirate_status[index] = health


def status():
    to_be_repaired = [i for i in pirate_status if i < 0.2 * health]
    print(f"{len(to_be_repaired)} sections need repair.")


pirate_status = [int(i) for i in input().split(">")]
warship_status = [int(i) for i in input().split(">")]
health = int(input())
while True:
    command = input().split()
    if command[0] == "Retire":
        break
    elif command[0] == "Fire":
        if len(warship_status) > int(command[1]) >= 0:
            fire(warship_status,int(command[1]), int(command[2]))
    elif command[0] == "Defend":
        if 0 <= int(command[1]) < len(pirate_status)\
                and 0 <= int(command[2]) < len(pirate_status) and int(command[3]) > 0:
            defend(pirate_status, int(command[1]),int(command[2]),int(command[3]))
    elif command[0] == "Repair":
        if 0 <= int(command[1]) < len(pirate_status) and int(command[2]) > 0:
            repair(pirate_status, int(command[1]), int(command[2]))
    elif command[0] == "Status":
        status()
if pirate_status and warship_status:
    print(f"Pirate ship status: {sum(pirate_status)}\nWarship status: {sum(warship_status)}")

# heart delivery
houses = list(map(int, input().split('@')))
command = input().split()
current = 0
while command[0] != "Love!":
    current += int(command[1])
    if current >= len(houses):
        current = 0
    if int(houses[current]) == 0:
        print(f"Place {current} already had Valentine's day.")
    else:
        houses[current] -= 2
        if houses[current] == 0:
            print(f"Place {current} has Valentine's day.")
    command = input().split()
print(f"Cupid's last position was {current}.")
if sum(houses) == 0:
    print("Mission was successful.")
else:
    failed = [int(h) for h in houses if int(h) != 0]
    print(f"Cupid has failed {len(failed)} places.")
