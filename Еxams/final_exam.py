import re
# string game
received_string = input()
while True:
    command = input().split()
    if command[0] == "Done":
        break
    elif command[0] == "Change":
        received_string = received_string.replace(command[1], command[2])
        print(received_string)
    elif command[0] == "Includes":
        if command[1] in received_string:
            print('True')
        else:
            print('False')
    elif command[0] == "End":
        if received_string.endswith(command[1]):
            print('True')
        else:
            print('False')
    elif command[0] == "Uppercase":
        received_string = received_string.upper()
        print(received_string)
    elif command[0] == "FindIndex":
        index = received_string.index(command[1])
        print(index)
    elif command[0] == "Cut":
        received_string = received_string[int(command[1]):(int(command[1])+int(command[2]))]
        print(received_string)

# message decrypter
n = int(input())
regex = r'^(\$|%)([A-Z][a-z]{2,})\1\:\s\[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|$'
for i in range(n):
    word = ''
    message = input()
    match = re.search(regex, message)
    if match:
        sign, main_part, num1, num2, num3 = match.groups()
        word = chr(int(num1)) + chr(int(num2)) + chr((int(num3)))
        print(f'{main_part}: {word}')
    else:
        print('Valid message not found!')

# messages manager
records = {}
message_limit = int(input())
while True:
    command = input().split('=')
    if command[0] == "Statistics":
        break
    elif command[0] == "Add":
        if command[1] not in records.keys():
            records[command[1]] = {'sent': int(command[2]), 'received': int(command[3])}
    elif command[0] == "Message":
        if command[1] in records.keys() and command[2] in records.keys():
            records[command[1]]['sent'] += 1
            records[command[2]]['received'] += 1
            if records[command[1]]['sent'] + records[command[1]]['received'] >= message_limit:
                records.pop(command[1])
                print(f"{command[1]} reached the capacity!")
            if records[command[2]]['sent'] + records[command[2]]['received'] >= message_limit:
                records.pop(command[2])
                print(f"{command[2]} reached the capacity!")
    elif command[0] == "Empty":
        if command[1] == "All":
            records.clear()
        else:
            if command[1] in records.keys():
                records.pop(command[1])
print(f"Users count: {len(records)}")
for k, v in records.items():
    print(f"{k} - {(v['received']+v['sent'])}")
