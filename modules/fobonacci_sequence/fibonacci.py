sequence_of_number = []


def create_sequence(number):
    sequence_of_number.clear()
    sequence_of_number.append(0)
    sequence_of_number.append(1)

    for _ in range(number - 2):
        sequence_of_number.append(
            sequence_of_number[-1] + sequence_of_number[-2]
        )

    return ' '.join(map(str, sequence_of_number))


def locate_number(element):
    if element in sequence_of_number:
        element_index = sequence_of_number.index(element)
        return f'The number - {element} is at index {element_index}'
    else:
        return f'The number {element} is not in the sequence'
