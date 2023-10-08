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