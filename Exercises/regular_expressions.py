import re
# match full name
names = input()
regex = "\\b[A-Z][a-z]+ [A-Z][a-z]+\\b"
matches = re.findall(regex, names)
print(' '.join(matches))

# match phone number
numbers = input()
regex = r"\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b"
matches = re.findall(regex, numbers)
print(', '.join(matches))

# match dates
dates = input()
regex = r'(\d{2})([-.\/])([A-Z][a-z]{2})\2(\d{4})'
matches = re.findall(regex, dates)
for match in matches:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")

# match numbers
input_string = input()
regex = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
matches = re.finditer(regex, input_string)
for match in matches:
    print(match.group(), end=" ")
