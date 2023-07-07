def calculate_average(numbers):
    total = 0
    for number in numbers:
        total += number
    average = total / len(numbers)
    return average

# # grades = [90, 85, 92, 78, 80]
# # average_grade = calculate_average(grades)
# # print("Average Grade:", average_grade)
# def double(x):
#    breakpoint()
#    return x * 2
# val = 3
# print(f"{val} * 2 is {double(val)}")