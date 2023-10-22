# cooking masterclass
from math import ceil
budget = float(input())
number_of_students = int(input())
flour_price = float(input())
egg_price = float(input())
apron_price = float(input())
free_flour = number_of_students // 5
price_of_aprons = int((apron_price * ceil(number_of_students*1.2)))
total_price = price_of_aprons + (egg_price*10*number_of_students) + (flour_price *(number_of_students - free_flour))
if total_price <= budget:
    print(f"Items purchased for {total_price:.2f}$.")
else:
    print(f"{abs(budget - total_price):.2f}$ more needed.")

# tax calculator
vehicles = input().split(">>")
total_taxes = 0
for i in vehicles:
    is_valid = True
    vehicle = i.split()
    current_taxes = 0
    if vehicle[0] == "family":
        year_reduce = 5 * int(vehicle[1])
        km_increase = 12 * (int(vehicle[2]) // 3000)
        current_taxes = km_increase + (50 - year_reduce)
    elif vehicle[0] == "heavyDuty":
        year_reduce = 8 * int(vehicle[1])
        km_increase = 14 * (int(vehicle[2]) // 9000)
        current_taxes = km_increase + (80 - year_reduce)
    elif vehicle[0] == "sports":
        year_reduce = 9 * int(vehicle[1])
        km_increase = 18 * (int(vehicle[2]) // 2000)
        current_taxes = km_increase + (100 - year_reduce)
    else:
        print("Invalid car type.")
        is_valid = False
        continue
    if is_valid:
        print(f"A {vehicle[0]} car will pay {current_taxes:.2f} euros in taxes.")
        total_taxes += current_taxes
print(f"The National Revenue Agency will collect {total_taxes:.2f} euros in taxes.")

# phone shop
phones = input().split(", ")
while True:
    command = input()
    if command == "End":
        break
    else:
        to_do = command.split(" - ")
        if to_do[0] == "Add":
            if to_do[1] not in phones:
                phones.append(to_do[1])
        elif to_do[0] == "Remove":
            if to_do[1] in phones:
                phones.remove(to_do[1])
        elif to_do[0] == "Bonus phone":
            two_phones = to_do[1].split(":")
            if two_phones[0] in phones:
                ind = phones.index(two_phones[0])
                phones.insert(ind+1, two_phones[1])
        elif to_do[0] == "Last":
            if to_do[1] in phones:
                phones.remove(to_do[1])
                phones.append(to_do[1])
print(", ".join(phones))
