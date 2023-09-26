# strange zoo
tail = input()
body = input()
head = input()
meerkat = [head, body, tail]
print(meerkat)

# courses
number = int(input())
courses = []
for i in range(number):
    current_course = input()
    courses.append(current_course)
print(courses)

# list statistics
n = int(input())
positives = []
negatives = []
for i in range(n):
    current_number = int(input())
    if current_number < 0:
        negatives.append(current_number)
    else:
        positives.append(current_number)
print(positives)
print(negatives)
print(f'''Count of positives: {len(positives)}
Sum of negatives: {sum(negatives)}''')

# search
n = int(input())
word = input()
strings = []
for i in range(n):
    current_string = input()
    strings.append(current_string)
print(strings)
for i in range(len(strings) - 1, -1, -1):
    element = strings[i]
    if word not in element:
        strings.remove(element)
print(strings)

# numbers filter
n = int(input())
numbers = []
for i in range(n):
    number = int(input())
    numbers.append(number)
command = input()
if command == "even":
    for i in range(len(numbers) - 1, -1, -1):
        counter = numbers[i]
        if counter % 2 != 0:
            numbers.remove(counter)
elif command == "odd":
    for i in range(len(numbers) - 1, -1, -1):
        counter = numbers[i]
        if counter % 2 == 0:
            numbers.remove(counter)
elif command == "positive":
    for i in range(len(numbers) - 1, -1, -1):
        counter = numbers[i]
        if counter < 0:
            numbers.remove(counter)
elif command == "negative":
    for i in range(len(numbers) - 1, -1, -1):
        counter = numbers[i]
        if counter >= 0:
            numbers.remove(counter)
print(numbers)

# other solution
n = int(input())
numbers = []
filtered = []
for i in range(n):
    number = int(input())
    numbers.append(number)
command = input()
if command == "even":
    for i in numbers:
        if i % 2 == 0:
            filtered.append(i)
elif command == "odd":
    for i in numbers:
        if i % 2 != 0:
            filtered.append(i)
elif command == "positive":
    for i in numbers:
        if i >= 0:
            filtered.append(i)
elif command == "negative":
    for i in numbers:
        if i < 0:
            filtered.append(i)
print(filtered)
