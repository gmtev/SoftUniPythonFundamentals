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


# other way to do it
def add_car(name, mileage, fuel):
    return {'name': name, 'mileage': mileage, 'fuel': fuel}


def drive(car, distance, required_fuel):
    if car['fuel'] >= required_fuel:
        car['mileage'] += distance
        car['fuel'] -= fuel
        print(f"{car['name']} driven for {distance} kilometers. {required_fuel} liters of fuel consumed.")
        if car['mileage'] > 100000:
            print(f"Time to sell the {car['name']}!")
            return True
        else:
            print("Not enough fuel to make that ride")

        return False


def refuel(car, added_fuel):
    max = 75
    fuel_added = min(added_fuel, max - car['fuel'])
    car['fuel'] += fuel_added
    print(f"{car['name']} refueled with {fuel_added} liters")


def revert(car, kilometers):
    car['mileage'] -= kilometers
    if car['mileage'] < 10000:
        car['mileage'] = 10000
    else:
        print(f"{car['name']} mileage decreased by {kilometers} kilometers")


def main_function():
    number_of_cars = int(input())
    cars = []
    for i in range(number_of_cars):
        car_info = input().split('|')
        car = add_car(car_info[0], int(car_info[1]), int(car_info[2]))
        cars.append(car)

    while True:
        command = input()
        if command == "Stop":
            break

        command = command.split(' : ')
        action = command[0]
        car_name = command[1]
        for car in cars:
            if car['name'] == car_name:
                if action == "Drive":
                    distance = int(command[2])
                    fuel = int(command[3])
                    if drive(car,distance,fuel):
                        cars.remove(car)
                elif action == "Refuel":
                    added_fuel = int(command[2])
                    refuel(car, added_fuel)
                elif action == "Revert":
                    kilometers = int(command[2])
                    revert(car, kilometers)

    for car in cars:
        print(f"{car['name']} -> Mileage: {car['mileage']} kms, Fuel in the tank: {car['fuel']} lt.")


main_function()

# mirror words
