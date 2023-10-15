# which are in?
seq_1 = input().split(", ")
seq_2 = input().split(", ")
seq_3 = []
for i in seq_1:
    for y in seq_2:
        if i in y:
            seq_3.append(i)
            break
print(seq_3)
print([i for i in seq_1 if any(i in y for y in seq_2)])

# next version
version = [int(digit) for digit in input().split(".")]
version[-1] += 1
# for index in range(len(version) -1, 0, -1):
#   if version[index] > 9:
#       version[index] = 0
#       version[index-1] += 1
if version[-1] > 9:
    version[-1] = 0
    version[-2] += 1
    if version[-2] > 9:
        version[-2] = 0
        version[0] += 1
# print(".".join(str(number for number in version)))
print(*version, sep=".")

# word_filter
words = input().split()
filtered_words = [word for word in words if len(word) % 2 == 0]
print(*filtered_words, sep="\n")
# print("\n".join(filtered_words))

# number classification
numbers = input().split(", ")
# positive = [i for i in numbers if int(i) >= 0]
# negative = [i for i in numbers if int(i) < 0]
# even = [i for i in numbers if int(i) % 2 == 0]
# odd = [i for i in numbers if int(i) % 2 != 0]
print(f"Positive: {', '.join([i for i in numbers if int(i) >= 0])}")
print(f"Negative: {', '.join([i for i in numbers if int(i) < 0])}")
print(f"Even: {', '.join([i for i in numbers if int(i) % 2 == 0])}")
print(f"Odd: {', '.join([i for i in numbers if int(i) % 2 != 0])}")

# office chairs


def room_checker(number_of_rooms):
    free = 0
    for room_num in range(1, number_of_rooms+1):
        free_chairs_current, visitors = input().split()
        dif = len(free_chairs_current) - int(visitors)
        if dif < 0:
            print(f"{abs(dif)} more chairs needed in room {room_num}")
        free += dif  # works as well with negative chairs
    return free


rooms = int(input())
total_free = room_checker(rooms)
if total_free >= 0:
    print(f"Game On, {total_free} free chairs left")
# without a function
rooms_1 = int(input())
free_1 = 0
for room_num_1 in range(1, rooms_1+1):
    free_chairs, visitors_1 = input().split()
    diff_1 = len(free_chairs) - int(visitors_1)
    if diff_1 < 0:
        print(f"{abs(diff_1)} more chairs needed in room {room_num_1}")
    free_1 += diff_1
if free_1 >= 0:
    print(f"Game On, {free_1} free chairs left")

# electron distribution
number_of_electrons = int(input())
shells = []
for shell in range(1, number_of_electrons+1):
    max_el = 2 * shell ** 2
    if number_of_electrons >= max_el:
        shells.append(max_el)
        number_of_electrons -= max_el
        if number_of_electrons == 0:
            break
    else:
        shells.append(number_of_electrons)
        break
print(shells)
# with "while" loop
number_of_electrons = int(input())
shells = []
shell = 1
while number_of_electrons > 0:
    max_el = 2 * shell ** 2
    shell += 1
    if number_of_electrons >= max_el:
        shells.append(max_el)
        number_of_electrons -= max_el
    else:
        shells.append(number_of_electrons)
        break
print(shells)

# Group of 10's
numbers_to_store = [int(digit) for digit in input().split(", ")]
current_limit = 10
while numbers_to_store:
    filtered = [i for i in numbers_to_store if i <= current_limit]
    print(f"Group of {current_limit}'s: {filtered}")
    current_limit += 10
    numbers_to_store = [digit for digit in numbers_to_store if digit not in filtered]

# decipher this
message = input().split()
deciphered_message = []
for i in message:
    numbers_to_decipher = [checker for checker in i if checker.isdigit()]
    words = [checker for checker in i if checker not in numbers_to_decipher]
    first_letter = chr(int(''.join(numbers_to_decipher)))
    words[0], words[-1] = words[-1], words[0]
    deciphered_word = first_letter + "".join(words)
    deciphered_message.append(deciphered_word)
print(' '.join(deciphered_message))

