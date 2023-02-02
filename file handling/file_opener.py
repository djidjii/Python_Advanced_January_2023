file_name = 'text.txt'

try:
    file = open(file_name, 'r')
    print('File found')
except FileExistsError:
    print('File not found')
