# no vowels
text = input()
no_vowels = [char for char in text if char.lower() not in ['a', 'e', 'i', 'o', 'u']]
print(''.join(no_vowels))

# trains
wagons = [0] * int(input())
while True:
    cmd = input().split()
    if cmd[0] == "End":
        print(wagons)
        break
    elif cmd[0] == "add":
        number_of_people = int(cmd[1])
        wagons[-1] += number_of_people
    elif cmd[0] == "insert":
        index = int(cmd[1])
        number_of_people = int(cmd[2])
        wagons[index] += number_of_people
    elif cmd[0] == "leave":
        index = int(cmd[1])
        number_of_people = int(cmd[2])
        wagons[index] -= number_of_people

# to-do list


def todo_list():
    to_do_list = []
    while True:
        note = input()
        if note == "End":
            break
        to_do_list.append(note)
    sorted_list = sorted(to_do_list, key=lambda x: int(x.split("-")[0]))
    return [task.split("-")[1] for task in sorted_list]


result = todo_list()
print(result)

# palindrome strings


def palindrome_finder(word):
    if word == word[::-1]:
        return word


words = input().split()
searched_word = input()
filtered_words = [word for word in words if palindrome_finder(word)]

print(filtered_words)
print(f'Found palindrome {words.count(searched_word)} times')

# sorting names
names = input().split(", ")
sorted_names = sorted(names, key=lambda x: (-len(x), x))
print(sorted_names)
# with function


def sorting_names():
    names = [name for name in input().split(", ")]
    return sorted(names, key=lambda x: (-len(x), x))


print(sorting_names())

# even numbers
numbers = [int(num) for num in input().split(", ")]
indexes = [numbers.index(i) for i in numbers if i % 2 == 0]
print(indexes)
# the other way to solve it
number_list = list(map(int, input().split(", ")))
found_indices_or_not = map(
    lambda x: x if number_list[x] % 2 == 0 else "no",
    range(len(number_list))
)
even_indices = list(filter(lambda a: a != "no", found_indices_or_not))
print(even_indices)

# the office


def employee_happiness_checker():
    happiness_list = list(map(int, input().split()))
    happiness_factor = int(input())
    improved_happiness = [happiness * happiness_factor for happiness in happiness_list]
    average = sum(improved_happiness) / len(improved_happiness)
    happiness_counter = sum(happiness >= average for happiness in improved_happiness)
    total_count = len(improved_happiness)
    message = "are happy!" if happiness_counter >= total_count/2 else "are not happy!"
    result = f"Score: {happiness_counter}/{total_count}. Employees {message}"
    return result


print(employee_happiness_checker())
