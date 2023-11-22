import re
# the imitation game
message = input()
while True:
    command = input()
    if command == "Decode":
        break
    else:
        command = command.split('|')
        if command[0] == "Move":
            number_of_letters = int(command[1])
            message = message[number_of_letters:] + message[:number_of_letters]
        elif command[0] == "Insert":
            index, value = int(command[1]), command[2]
            message = message[:index] + value + message[index:]
        elif command[0] == "ChangeAll":
            substring, replacement = command[1], command[2]
            message = message.replace(substring, replacement)
print(f"The decrypted message is: {message}")

# fancy barcodes
number_of_barcodes = int(input())
regex = r'(@#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(@#+)'
for barcode in range(number_of_barcodes):
    product_group = ''
    has_digit = False
    current_barcode = input()
    match = re.search(regex, current_barcode)
    if match:
        for i in current_barcode:
            if i.isnumeric():
                product_group += str(i)
                has_digit = True
        if not has_digit:
            product_group = "00"
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")

# need for speed III
number_of_cars = int(input())
cars = {}
for car in range(number_of_cars):
    car_model, mileage, fuel = input().split('|')
    cars[car_model] = [int(mileage), int(fuel)]
while True:
    command = input()
    if command == "Stop":
        break
    else:
        command = command.split(' : ')
        if command[0] == "Drive":
            if int(command[3]) > (cars[command[1]][1]):
                print("Not enough fuel to make that ride")
            else:
                cars[command[1]][0] += int(command[2])
                cars[command[1]][1] -= int(command[3])
                print(f"{command[1]} driven for {command[2]} kilometers. {command[3]} liters of fuel consumed.")
            if cars[command[1]][0] >= 100000:
                print(f"Time to sell the {command[1]}!")
                cars.pop(command[1])
        elif command[0] == "Refuel":
            if cars[command[1]][1] + int(command[2]) > 75:
                added = 75 - cars[command[1]][1]
            else:
                added = int(command[2])
            cars[command[1]][1] += added
            print(f"{command[1]} refueled with {added} liters")
        elif command[0] == "Revert":
            cars[command[1]][0] -= int(command[2])
            if cars[command[1]][0] < 10000:
                cars[command[1]][0] = 10000
            else:
                print(f"{command[1]} mileage decreased by {command[2]} kilometers")
for car, stats in cars.items():
    print(f"{car} -> Mileage: {stats[0]} kms, Fuel in the tank: {stats[1]} lt.")