# Zeros to Back (this one gave me only 80/100, wouldn't pass only one test)
line = input().split(", ")
for zero_checker in line:
    if "0" in zero_checker:
        line.remove(zero_checker)
        line.append("0")
line = [eval(i) for i in line]
print(line)
# the one that gave me 100/100
line = input().split(", ")
line = [eval(i) for i in line]
zero_count = line.count(0)
line = [num for num in line if num != 0]
line.extend([0] * zero_count)
print(line)

# Tic-Tac-Toe
first_line = input().split(" ")
second_line = input().split(" ")
third_line = input().split(" ")
if first_line[0] == first_line[1] == first_line[2] == "1" or first_line[0] == second_line[0] == third_line[0] == "1"\
    or first_line[1] == second_line[1] == third_line[1] == "1" or first_line[2] == second_line[2] == third_line[2]\
    == "1" or second_line[0] == second_line[1] == second_line[2] == "1" or third_line[0] == third_line[1] == \
    third_line[2] == "1" or first_line[0] == second_line[1] == third_line[2] == "1" or first_line[2] == \
        second_line[1] == third_line[0] == "1":
    print("First player won")
elif first_line[0] == first_line[1] == first_line[2] == "2" or first_line[0] == second_line[0] == third_line[0] == "2"\
    or first_line[1] == second_line[1] == third_line[1] == "2" or first_line[2] == second_line[2] == third_line[2]\
    == "2" or second_line[0] == second_line[1] == second_line[2] == "2" or third_line[0] == third_line[1] == \
    third_line[2] == "2" or first_line[0] == second_line[1] == third_line[2] == "2" or first_line[2] == \
        second_line[1] == third_line[0] == "2":
    print("Second player won")
else:
    print("Draw!")
