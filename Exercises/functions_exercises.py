# smallest of three numbers
n1, n2, n3 = int(input()), int(input()), int(input())


def smallest_of_three_numbers(a,b,c):
    return min(a, b, c)


print(smallest_of_three_numbers(n1, n2, n3))

# add and subtract
number_1, number_2, number_3 = int(input()), int(input()), int(input())


def sum_numbers(a,b):
    return a + b


def subtract(c,d):
    return c - d


def add_and_subtract(a,b,c):
    summed = sum_numbers(a,b)
    return subtract(summed,c)


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
        elif i %2 != 0:
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