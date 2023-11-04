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
dic = dict(zip(countries, capitals))
for k, v in dic.items():
    print(f'{k} -> {v}')

# phonebook
phonebook = {}
cmd = input()
while len(cmd) > 2:
    name, phone = cmd.split('-')
    phonebook[name] = phone
    cmd = input()
for i in range(int(cmd)):
    contact = input()
    if contact in phonebook.keys():
        print(f'{contact} -> {phonebook[contact]}')
    else:
        print(f"Contact {contact} does not exist.")
