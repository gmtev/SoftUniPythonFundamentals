# smallest of three numbers
n1, n2, n3 = int(input()), int(input()), int(input())


def smallest_of_three_numbers(a,b,c):
    return min(a, b, c)


print(smallest_of_three_numbers(n1, n2, n3))

# add and subtract
number_1, number_2, number_3 = int(input()), int(input()), int(input())


def sum_numbers(a, b):
    return a + b


def subtract(c, d):
    return c - d


def add_and_subtract(a, b, c):
    summed = sum_numbers(a, b)
    return subtract(summed, c)


print(add_and_subtract(number_1, number_2, number_3))

# chars in range
char = input()
char2 = input()


def char_range(a, b):
    for i in range(ord(a) + 1, ord(b)):
        print(chr(i), end=" ")


char_range(char, char2)

# # odd and even sum
given_number = input()


def odd_and_even_sum(num):
    odd = 0
    even = 0
    for i in num:
        i = int(i)
        if i % 2 == 0:
            even += i
        elif i % 2 != 0:
            odd += i
    return f"Odd sum = {odd}, Even sum = {even}"


print(odd_and_even_sum(given_number))

# even_numbers_filter
numbers = [int(i) for i in input().split()]
even = []


def even_finder(num):
    if num % 2 == 0:
        return True
    else:
        return False


even_numbers = filter(even_finder, numbers)
for i in even_numbers:
    even.append(i)
print(even)

# sort

numbers = [int(i) for i in input().split()]
print(sorted(numbers))

# Min, Max and Sum

numbers = [int(i) for i in input().split()]
print(f"The minimum number is {min(numbers)}")
print(f"The maximum number is {max(numbers)}")
print(f"The sum number is: {sum(numbers)}")

# Palindrome integers
integers = [int(i) for i in input().split(", ")]


def palindrome_integers_checker(num):
    num = str(num)
    if num == num[::-1]:
        return True
    else:
        return False


for i in integers:
    print(palindrome_integers_checker(i))

# Password validator
password = input()


def password_validator(check):
    list_of_errors = []
    if len(check) < 6 or len(check) > 10:
        list_of_errors.append("Password must be between 6 and 10 characters")
    if any(not i.isalnum() for i in check):
        list_of_errors.append("Password must consist only of letters and digits")
    if sum(i.isdigit() for i in check) < 2:
        list_of_errors.append("Password must have at least 2 digits")
    return list_of_errors


password_checker = password_validator(password)
if not password_checker: # if list of errors is empty
    print("Password is valid")
else:
    print("\n".join(password_checker))


# Perfect number
number = int(input())


def is_perfect(num):
    divisors_sum = 0
    for divisor in range(1, num):
        if num % divisor == 0:
            divisors_sum += divisor
    if num == divisors_sum:
        return "We have a perfect number!"
    return "It's not so perfect."


print(is_perfect(number))


# Loading bar
number = int(input())


def loading_bar(num:int) -> str:
    if num == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    loaded_percent = num // 10
    return f"{num}% [{'%'*loaded_percent}{'.'*(10 - loaded_percent)}]\nStill loading..."


print(loading_bar(number))

# Factorial division


def factorials (num):
    for i in range(1, num):
        num *= i
    return num


first_number = int(input())
second_number = int(input())


print(f"{factorials(first_number)/(factorials(second_number)):.2f}")
