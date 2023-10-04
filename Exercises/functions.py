# absolute values
numbers = input().split()
absolute_numbers = []
for number in numbers:
    absolute_numbers.append(abs(float(number)))
print(absolute_numbers)


# grades
grade_data = float(input())


def grade_checker(grade_value):
    if 2.00 <= grade_value <= 2.99:
        return "Fail"
    elif 3.00 <= grade_value <= 3.49:
        return "Poor"
    elif 3.50 <= grade_value <= 4.49:
        return "Good"
    elif 4.50 <= grade_value <= 5.49:
        return "Very Good"
    elif 5.50 <= grade_value <= 6.00:
        return "Excellent"


print(grade_checker(grade_data))

# calculator
command = input()
first_number = int(input())
second_number = int(input())


def calculator(operator, a, b):
    result = None
    if operator == "multiply":
        result = a * b
    elif operator == "divide":
        result = int(a/b)
    elif operator == "subtract":
        result = a - b
    elif operator == "add":
        result = a + b
    return result


print(calculator(command, first_number, second_number))

# repeat string
repeat_strings = lambda given_string, amount: given_string * amount
example_string = input()
count = int(input())
repeated_strings = repeat_strings(example_string, count)
print(repeated_strings)
# print(repeat_string(example_string, count))

# orders
drink = input()
quantity = int(input())


def orders(type, amount):
    if type == "coke":
        return f"{(amount * 1.40):.2f}"
    elif type == "coffee":
        return f"{(amount * 1.50):.2f}"
    elif type == "water":
        return f"{(amount * 1.00):.2f}"
    elif type == "snacks":
        return f"{(amount * 2.00):.2f}"


print(orders(drink, quantity))

# calculate rectangle area
wd = int(input())  # width
ln = int(input())  # length


def rectangle_area_finder(width, length):
    return width * length


print(rectangle_area_finder(wd, ln))
# rounding
list_of_numbers = [float(num) for num in input().split(" ")]
rounded_numbers = []
for _ in list_of_numbers:
    rounded_numbers.append(round(_))
print(rounded_numbers)
