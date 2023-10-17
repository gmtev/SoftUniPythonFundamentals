# binary digits count
def bit_solve(number, digit):
    count = 0
    while number > 0:
        remainder = number % 2
        number = number // 2
        if remainder == digit:
            count += 1
    return count


number_to_solve = int(input())
print(bit_solve(number_to_solve, 0))
# second option
num = (bin(int(input())))
zero_counter = 0
num_splitter = num.split("b")
for i in num_splitter[1]:
    if i == "0":
        zero_counter += 1
print(zero_counter)

# bit at position 1


def bit_at_1(num):
    num = bin(num)
    n = num[-2]
    return n


number = int(input())
bit_at_1(number)