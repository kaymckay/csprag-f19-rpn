#!/usr/bin/env python3
import sys
from termcolor import colored, cprint

def calculate(arg):
    stack = list()
    for token in arg.split():
        if token == '+':
            arg1 = stack.pop()
            arg2 = stack.pop()
            result = arg1 + arg2
            stack.append(result)
            output = colored(stack, 'magenta')
            print(output)
        elif token == '-':
            arg1 = stack.pop()
            arg2 = stack.pop()
            result = arg2 - arg1
            stack.append(result)
            output = colored(stack, 'green')
            print(output)
        elif token == '*':
	    arg1 = stack.pop()
            arg2 = stack.pop()
            result = arg2 - arg1
            stack.append(result)
            output = colored(stack, 'green')
            print(output)
        else:
            stack.append(int(token))
    if len(stack) != 1:
        cprint(stack, 'white', 'on_red')
        raise TypeError('Malformed input ' + arg)
    return stack.pop()

def main():
    while True:
        calculate(input("rpn calc> "))

if __name__ == '__main__':
    main()

