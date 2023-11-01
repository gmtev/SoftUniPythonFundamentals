# bakery
stock = input().split()
goods_info = {}
for i in range(0, len(stock), 2):
    key = stock[i]
    value = stock[i+1]
    goods_info[key] = int(value)
print(goods_info)

# stock
stock = input().split()
goods_info = {}
for i in range(0, len(stock), 2):
    key = stock[i]
    value = stock[i+1]
    goods_info[key] = int(value)
searched_for = input().split()
for i in searched_for:
    if i in goods_info:
        print(f"We have {goods_info[i]} of {i} left")
    else:
        print(f"Sorry, we don't have {i}")

# statistics
products = {}
while True:
    cmd = input()
    if cmd == "statistics":
        break
    else:
        tokens = cmd.split(': ')
        product = tokens[0]  # key
        quantity = int(tokens[1])  # value
        if product not in products:
            products[product] = 0
        products[product] += quantity
print("Products in stock:")
for product, quantity in products.items():
    print(f"- {product}: {quantity}")  # (print(f"- {product}: {quantity}") for (product, quantity) in products)
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")

# students
info = input()
students = []
course = ''
while True:
    if ':' not in info:
        course = info
        break
    else:
        info.split(':')
        name, id, course = info.split(':')
        students.append({'name': name, 'id': id, 'course': course})
        info = input()
for student in students:
    if course.startswith(student['course'][0:3]):
        print(f"{student['name']} - {student['id']}")

# ascii values
chars = input().split(', ')
dic = {char: ord(char) for char in chars}
print(dic)

# odd occurrences
words = input().split()
dictionary = {}
for i in words:
    if i.lower() not in dictionary:
        dictionary[i.lower()] = 0
    dictionary[i.lower()] += 1
for k, v in dictionary.items():
    if v % 2 != 0:
        print(k, end=' ')
