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
