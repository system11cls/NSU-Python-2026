from sys import argv, stderr

if len(argv) < 2:
    print("No limit set", file=stderr)
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
    N = int(argv[1])
    primes = [prime for prime in range(2, N) if is_simple(prime)]
    print(primes)
except ValueError:
    print("arg is not an int", file=stderr)
    exit(1)
