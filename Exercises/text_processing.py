# reverse strings
while True:
    word = input()
    if word == "end":
        break
    print(f"{word} = {word[::-1]}")

# without slicing
while True:
    word = input()
    if word == "end":
        break
    reversed_word = ""
    for i in reversed(word):
        reversed_word += i
    print(f"{word} = {reversed_word}")

# Repeat Strings
sequence = input().split()
for i in sequence:
    print(i * len(i), end="")

# substring
first = input()
second = input()
while first in second:
    second = second.replace(first, "")
print(second)

# text filter
banned_words = input().split(', ')
text = input()
for word in banned_words:
    while word in text:
        text = text.replace(word, '*' * len(word))
print(text)

# digits, letters and others
sequence = input()
digits = ""
letters = ""
others = ""
for i in sequence:
    if i.isalpha():
        letters += i
    elif i.isdigit():
        digits += i
    else:
        others += i
print(f"{digits}\n{letters}\n{others}")
