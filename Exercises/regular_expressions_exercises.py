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

# find occurrences of word in sentence
sentence = input()
word = input()
regex = fr"(?i)\b{word}\b"  # ignorecase flag
word_in_sentence = re.findall(regex, sentence, )
print(len(word_in_sentence))

# extract emails
sentence = input()
regex = r"\s(([a-z0-9]+[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b"  # everything is put in a group for the printing
valid_emails = re.findall(regex, sentence)
for email in valid_emails:
    print(email[0])

# furniture
furniture = input()
bought_furniture = []
total_cost = 0
regex = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"
while furniture != "Purchase":
    match = re.search(regex, furniture)
    if match:
        item, price, quantity = match.groups()
        bought_furniture.append(item)
        total_cost += float(price) * float(quantity)
    furniture = input()
print(f"Bought furniture:")
for item in bought_furniture:
    print(item)
print(f"Total money spend: {total_cost:.2f}")

# extract the links
links_and_text = input()
regex = r'\b(www.[a-zA-Z0-9\-]+(\.[a-z]+)+)\b'
while links_and_text:
    match = re.search(regex, links_and_text)
    if match:
        link = match.group(0)
        print(link)
    links_and_text = input()
