#  exchange integers
first_int = int(input())
second_int = int(input())
print(f'''Before:
a = {first_int}
b = {second_int}''')
helping_variable = first_int
first_int = second_int
print(f'''After:
a = {first_int}
b = {helping_variable}''')

#  prime number guesser
number = int(input())
non_prime = False
if number == 1:
    print("False")
for i in range(2, number):
    if (number % i) == 0:
        non_prime = True
        break
if non_prime:
    print("False")
else:
    print("True")  # as in "number is prime"

#  decrypting messages
key = int(input())
lines = int(input())
message = ""
for i in range(lines):
    letter = input()
    ascii_number = ord(letter)
    new_letter = chr(ascii_number + key)
    message += new_letter
print(message)

#  balanced brackets
n_of_lines = int(input())
opening = 0
closing = 0
last_bracket = ""
flag = False
for i in range(0, n_of_lines):
    symbol = input()
    if symbol == "(":
        opening += 1
    if symbol == ")":
        closing += 1
    if last_bracket == symbol:
        print("UNBALANCED")
        flag = True
        break
    last_bracket = symbol
if not flag:
    if closing == opening:
        print("BALANCED")
    else:
        print("UNBALANCED")


#  since the upper one didn't always pass all the tests, I've included an alternative solution too
number_if_lines = int(input())
flag = True  # as in " it's balanced"
last_bracket = ''
for i in range(0, number_if_lines):
    symbol = input()
    if symbol not in ['(', ')']:
        continue
    if last_bracket == '' and symbol == ')' or last_bracket == symbol:
        flag = False
        break
    last_bracket = symbol
if flag:
    print('BALANCED')
else:
    print('UNBALANCED')