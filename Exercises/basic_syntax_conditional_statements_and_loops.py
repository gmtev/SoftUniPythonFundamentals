# number definer
n = float(input())
if n == 0:
    print("zero")
elif n >= 0:
    if n < 1:
        print("small positive")
    elif n > 1000000:
        print("large positive")
    else:
        print("positive")
else:
    if abs(n) < 1:
        print("small negative")
    elif abs(n) > 1000000:
        print("large negative")
    else:
        print("negative")

# largest of three numbers
n1, n2, n3 = int(input()), int(input()), int(input())
print(max(n1, n2, n3))

# word reverse
word = input()
print(word[::-1])

# even numbers
n = int(input())
for i in range(n):
    number = int(input())
    if not number % 2 == 0:
        print(f"{number} is odd!")
        break
else:
    print("All numbers are even.")

# number between 1 and 100
n = float(input())
while n < 1 or n > 100:
    n = float(input())
print(f"The number {n} is between 1 and 100")

# shopping
budget = int(input())
while True:
    command = input()
    if command == "End":
        print("You bought everything needed.")
        break
    else:
        price = int(command)
        budget -= price
    if budget < 0:
        print("You went in overdraft!")
        break

# patterns
n = int(input())
for i in range(1, n+1):
    for y in range(0, i):
        print("*", end="")
    print()
for i in range(n-1, 0, -1):
    for y in range(0, i):
        print("*", end="")
    print()
    