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