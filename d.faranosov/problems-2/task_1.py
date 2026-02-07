
def is_numeric(str) -> bool:
    try:
        float(str)
        return True
    except ValueError:
        return False

while True:
    try:
        str = input()
        if is_numeric(str):
            print("numeric got")
            exit(0)
        else:
            print("Value is not a numeric")
    except EOFError:
        print("EOF got")
        exit(1)