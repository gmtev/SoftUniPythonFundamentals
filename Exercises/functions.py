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
