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


