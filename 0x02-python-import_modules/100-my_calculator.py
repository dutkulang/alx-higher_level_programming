#!/usr/bin/python3

def my_calculator():
    import sys
    from calculator_1 import add, mul, div, sub

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])
    
    if len(sys.argv) != 4:
        print("Usage: {0} <a> operator <b>".format(sys.argv[0]))
        sys.exit(1)

    if operator == '+':
        print("{0:d} + {1:d} = {2:d}".format(a, b, add(a, b)))
    elif operator == '*':
        print("{0:d} * {1:d} = {2:d}".format(a, b, mul(a, b)))
    elif operator == '/':
        print("{0:d} / {1:d} = {2:d}".format(a, b, div(a, b)))
    elif operator == '-':
        print("{0:d} - {1:d} = {2:d}".format(a, b, sub(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(0)

if __name__ == "__main__":
    my_calculator()
