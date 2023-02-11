import operator as op


def mathematical_operations(first_number, operator, second_number):
    first_number, second_number = int(first_number), int(second_number)
    valid_operators = {'+': op.add, '-': op.sub, '^': op.xor, '*': op.mul, '/': op.truediv}

    return valid_operators[operator](first_number, second_number)
