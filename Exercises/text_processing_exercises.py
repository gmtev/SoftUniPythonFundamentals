# valid usernames
def valid_username(username):
    length = False
    symbols = True
    if 3 <= len(username) <= 16:
        length = True
    for character in username:
        if not (character.isalnum() or character == "-" or character == "_") or character == "@" or character == " ":
            symbols = False
    if symbols and length:
        return True


usernames = input().split(", ")
for i in usernames:
    if valid_username(i):
        print(i)

# character multiplier
first, second = input().split()
total_sum = 0
if len(first) > len(second):
    for i in range(len(second)):
        total_sum += ord(first[i]) * ord(second[i])
    for i in range(len(second), len(first)):
        total_sum += ord(first[i])
elif len(first) < len(second):
    for i in range(len(first)):
        total_sum += ord(first[i]) * ord(second[i])
    for i in range(len(first), len(second)):
        total_sum += ord(second[i])
else:
    for i in range(len(first)):
        total_sum += ord(first[i]) * ord(second[i])
print(total_sum)

# extract file
file_path = input().split("\\")
file_name_and_extension = file_path[-1]
file_name, file_extension = file_name_and_extension.split('.')
print(f"File name: {file_name}\nFile extension: {file_extension}")

# caesar cipher
message = input()
encrypted_message = ""
for i in message:
    encrypted_message += chr(ord(i) + 3)
print(encrypted_message)

# emoticon finder
message = input()
for i in range(len(message)):
    if message[i] == ":":
        print(f"{message[i]}{message[i+1]}")

# replace repeating chars
chars = input()
filtered = ''
last_char = ""
for i in chars:
    if i != last_char or len(filtered) == 0:
        filtered += i
    last_char = i
print(filtered)

# string explosion
pre_explosion_string = input()
output = ""
explosion = 0
for i in range(len(pre_explosion_string)):
    if pre_explosion_string[i] == ">":
        explosion += int(pre_explosion_string[i + 1])
        output += pre_explosion_string[i]
    elif pre_explosion_string[i] != ">" and explosion > 0:
        explosion -= 1
    else:
        output += pre_explosion_string[i]
print(output)

# letters change numbers
alphabet = "abcdefghijklmnopqrstuvwxyz"
strings = [word.strip() for word in input().split()]
sum_of_words = 0
for word in strings:
    first_letter = word[0]
    last_letter = word[-1]
    number = int(word[1:-1])
    first_letter_index = alphabet.index(first_letter.lower()) + 1
    last_letter_index = alphabet.index(last_letter.lower()) + 1
    if first_letter.isupper():
        number /= first_letter_index
    elif first_letter.islower():
        number *= first_letter_index
    if last_letter.isupper():
        number -= last_letter_index
    elif last_letter.islower():
        number += last_letter_index
    sum_of_words += number
print(f'{sum_of_words:.2f}')

# rage quit
message = input()
rage_message = ""
repetitions = ''
current = ""
for i in range(len(message)):
    if not message[i].isdigit():
        current += message[i].upper()
    else:
        for next_symbol in range(i, len(message)):
            if not message[next_symbol].isdigit():
                break
            repetitions += message[next_symbol]
        rage_message += current * int(repetitions)
        current = ''
        repetitions = ''
print(f"Unique symbols used: {len(set(rage_message))}")
print(rage_message)


# winning ticket
def ticket_checker(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    winning_symbols = ["@", "#", "$", "^"]
    left_part = ticket[:10]
    right_part = ticket[10:]
    for matched in winning_symbols:
        for uninterrupted_matched in range(10, 5, -1):
            winning_symbol_repetition = matched * uninterrupted_matched
            if winning_symbol_repetition in left_part and winning_symbol_repetition in right_part:
                if uninterrupted_matched == 10:
                    return f'ticket "{ticket}" - {uninterrupted_matched}{matched} Jackpot!'
                return f'ticket "{ticket}" - {uninterrupted_matched}{matched}'
    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(', ')]
for current_ticket in tickets:
    print(ticket_checker(current_ticket))