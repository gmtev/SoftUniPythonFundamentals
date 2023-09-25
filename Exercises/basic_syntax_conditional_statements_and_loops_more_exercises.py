#  find the largest
number = input()
new_number = []
for i in range(len(number)):
    new_number.append(number[i])
new_number.sort(reverse=True)
for y in range(len(new_number)):
    print(new_number[y], end="")

#  find the capitals
word = input()
caps = []
for i in range(len(word)):
    if word[i].isupper():
        caps.append(i)
print(caps)

#  wolf in sheep's clothing
animals = input().split(", ")
wolf_index = animals.index('wolf') + 1
sheep_index = len(animals) - wolf_index
if wolf_index == len(animals):
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {sheep_index}! You are about to be eaten by a wolf!")

#  sum of a beach
word = input()
lower_case_word = word.casefold()
counter = 0

for word in ('sand', 'water', 'fish', 'sun'):
    counter += lower_case_word.count(word)

print(counter)
