def numbers_sum(file_name):
    data = open(file_name, 'r')
    sum_numbers = 0

    for number in data:
        sum_numbers += int(number)

    return sum_numbers


result = numbers_sum('txt.txt')
print(result)
