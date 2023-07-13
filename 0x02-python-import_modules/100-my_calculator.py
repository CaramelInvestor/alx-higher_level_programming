#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if (len(sys.argv)) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if (len(sys.argv[1])) != +:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
