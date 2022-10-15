list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22,
                -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_ind = 0
max_number = 0
for ind, current_number in enumerate(list_numbers):
    if current_number > max_number:
        max_ind = ind
        max_number = current_number
list_numbers[-1], list_numbers[max_ind] = list_numbers[max_ind], list_numbers[-1]
# TODO Оформить решение

print(list_numbers)
