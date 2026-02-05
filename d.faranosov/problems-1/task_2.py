from sys import argv, stderr

if len(argv) < 2:
    print("No number to work with", file=stderr)
    exit(1)

def is_simple(number: int):
    number = abs(number)
    for pretendent in range(2, number // 2):
        if number % pretendent == 0:
            return False
    if number > 1:
        return True
    return False

try:
    number = int(argv[1])
    print(f'{is_simple(number)}')
except ValueError:
    print(f'{argv[1]} is not an integer number', file=stderr)
    exit(1)