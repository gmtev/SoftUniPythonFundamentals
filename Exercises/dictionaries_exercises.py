# count char in string
text = input()
dic = {}
for i in text:
    if i != ' ':
        dic[i] = text.count(i)
for k, v in dic.items():
    print(f'{k} -> {int(v)}')

# a miner task
ores = {}
turn = 0
cmd = input()
while cmd != "stop":
    if turn == 0 or turn % 2 == 0:
        if cmd not in ores:
            ores[cmd] = int(0)
        last_ore = cmd
    else:
        if last_ore in ores:
            ores[last_ore] += int(cmd)
    turn += 1
    cmd = input()
for k, v in ores.items():
    print(f'{k} -> {int(v)}')

# capitals
countries = input().split(', ')
capitals = input().split(', ')
dic = dict(zip(countries, capitals))  # dic = {countries[index]: capitals[index] for index in range(len(countries))}
for k, v in dic.items():
    print(f'{k} -> {v}')

# phonebook
phonebook = {}
while True:
    cmd = input()
    if '-' not in cmd:
        break
    name, phone = cmd.split('-')
    phonebook[name] = phone
for i in range(int(cmd)):
    contact = input()
    if contact in phonebook.keys():
        print(f'{contact} -> {phonebook[contact]}')
    else:
        print(f"Contact {contact} does not exist.")

# legendary farming
items = {"shards": 0, "fragments": 0, "motes": 0}
flag = False
while not flag:
    farm_sesh = input().split()
    for i in range(0, len(farm_sesh), 2):
        v = int(farm_sesh[i])
        k = farm_sesh[i+1].lower()
        if k not in items.keys():
            items[k] = 0
        items[k] += int(v)
        if items['shards'] >= 250:
            print('Shadowmourne obtained!')
            items['shards'] -= 250
            flag = True
        elif items['fragments'] >= 250:
            print('Valanyr obtained!')
            items['fragments'] -= 250
            flag = True
        elif items['motes'] >= 250:
            print('Dragonwrath obtained!')
            items['motes'] -= 250
            flag = True
        if flag:
            break
for k,v in items.items():
    print(f'{k}: {int(v)}')

# force book
force_sides = {}
cmd = input()
while cmd != "Lumpawaroo":
    if '|' in cmd:
        side, user = cmd.split(' | ')
        user_taken = False
        for i in force_sides.values():
            if user in i:
                user_taken = True
                break
        if not user_taken:
            if side not in force_sides.keys():
                force_sides[side] = []
            force_sides[side].append(user)
    elif '->' in cmd:
        user, side = cmd.split(' -> ')
        for i in force_sides.values():
            if user in i:
                i.remove(user)
                break
        if side not in force_sides.keys():
            force_sides[side] = []
        force_sides[side].append(user)
        print(f"{user} joins the {side} side!")
    cmd = input()
for side, users in force_sides.items():
    if len(users) > 0:
        print(f"Side: {side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")
