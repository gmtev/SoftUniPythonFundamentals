import re
# capture the numbers
numbers_and_other = input()
while numbers_and_other:
    regex = r"\d+"
    match = re.findall(regex, numbers_and_other)
    if match:
        print(' '.join(match), end=" ")
    numbers_and_other = input()

# find variable name in sentence
sentence = input()
regex = r'\b_([A-Za-z0-9]+)\b'
variables = re.findall(regex, sentence)
print(','.join(variables))
