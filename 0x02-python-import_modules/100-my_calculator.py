#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    ac = len(sys.argv) - 1
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]
    if ac != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
    if op == '+':
        print('{} {} {} = {}'.format(a, b, op,  add(a, b)))
    elif op == '-':
        print('{} {} {} = {}'.format(a, b, op, sub(a, b)))
    elif op == '*':
        print('{} {} {} = {}'.format(a, b, op,  mul(a, b)))
    elif op == '/':
        print('{} {} {} = {}'.format(a, b, op, div(a, b)))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
