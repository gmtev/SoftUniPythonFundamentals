import re
# world tour
stops = input()
while True:
    command = input()
    if command == "Travel":
        break
    command = command.split(':')
    if command[0] == "Add Stop":
        if int(command[1]) in range(len(stops)):
            stops = stops[:int(command[1])] + command[2] + stops[int(command[1]):]
    elif command[0] == "Remove Stop":
        if int(command[2]) in range(len(stops)) and int(command[1]) in range(len(stops)):
            stops = stops[:int(command[1])] + stops[int(command[2])+1:]
    elif command[0] == "Switch":
        stops = stops.replace(command[1], command[2])
    print(stops)
print(f"Ready for world tour! Planned stops: {stops}")

# ad astra
food = input()
regex = r"(\#|\|)([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,4}|10000)\1"
matches = re.findall(regex,food)  # remember to use this
calories = sum([int(match[3]) for match in matches])
days = calories // 2000
print(f"You have food to last you for: {days} days!")
for match in matches:
    print(f"Item: {match[1]}, Best before: {match[2]}, Nutrition: {match[3]}")
