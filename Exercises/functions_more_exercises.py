# Data types


def data_type(cmd, inp):
    if cmd == "int":
        inp = int(inp)*2
        return inp
    elif cmd == "real":
        inp = float(inp) * 1.5
        return f"{inp:.2f}"
    elif cmd == "string":
        return f"${inp}$"


cmd = input()
inp = input()
print(data_type(cmd,inp))

# center point
from math import floor
X1 = float(input())
Y1 = float(input())
X2 = float(input())
Y2 = float(input())


def cartesian(x1, y1, x2, y2: float):
    x1, x2 = floor(x1), floor(x2)
    y1, y2 = floor(y1), floor(y2)
    return f"({min(x1, x2, key=abs)}, {min(y1, y2, key=abs)})"


print(cartesian(X1, Y1, X2, Y2))

# Tribonacci Sequence
def tribonacci(counter):
    if counter == 0 or counter == 1:
        return 1
    elif counter == 2:
        return 2
    elif counter == 3:
        return 4
    else:
        return (tribonacci(counter - 1) +
                tribonacci(counter - 2) +
                tribonacci(counter - 3))

n = int(input())
for i in range(n):
    print(tribonacci(i), end=" ")

# Multiplication Sign


def mult_sign(n1, n2, n3):
    if n1 == 0 or n2 == 0 or n3 == 0:
        return "zero"
    numbers = [n1, n2, n3]
    negative = 0
    for num in numbers:
        if num < 0:
            negative += 1
    if negative == 1 or negative == 3:
        return "negative"
    else:
        return "positive"



int1 = int(input())
int2 = int(input())
int3 = int(input())
print(mult_sign(int1, int2, int3))