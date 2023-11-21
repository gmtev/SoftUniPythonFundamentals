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