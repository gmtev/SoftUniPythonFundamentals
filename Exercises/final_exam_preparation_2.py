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

# p!rates
cities = {}
info = input().split("||")
while info[0] != "Sail":
    name, population, gold = info[0], int(info[1]), int(info[2])
    if name not in cities.keys():
        cities[name] = {"population": 0, "gold":0}
    cities[name]["population"] += population
    cities[name]["gold"] += gold
    info = input().split("||")
event = input().split('=>')
while event[0] != "End":
    command = event[0]
    if command == "Plunder":
        city_to_plunder, people_killed, gold_looted = event[1], int(event[2]), int(event[3])
        print(f"{city_to_plunder} plundered! {gold_looted} gold stolen, {people_killed} citizens killed.")
        cities[city_to_plunder]["population"] -= people_killed
        cities[city_to_plunder]["gold"] -= gold_looted
        if cities[city_to_plunder]["population"] == 0 or cities[city_to_plunder]["gold"] == 0:
            cities.pop(city_to_plunder)
            print(f"{city_to_plunder} has been wiped off the map!")
    elif command == "Prosper":
        town_to_prosper, gold_added = event[1], int(event[2])
        if gold_added < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities[town_to_prosper]["gold"] += gold_added
            print(f"{gold_added} gold added to the city treasury. {town_to_prosper} now has {cities[town_to_prosper]['gold']} gold.")
    event = input().split('=>')
if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city, city_info in cities.items():
        print(f"{city} -> Population: {city_info['population']} citizens, Gold: {city_info['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
