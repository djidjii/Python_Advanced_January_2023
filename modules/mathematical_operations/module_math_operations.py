from math_operations import mathematical_operations

try:
    data = mathematical_operations(*input('Please enter: first number, operator, second number: ').split(' '))
    print(data)
except ValueError:
    print('Enter a valid data!')
