#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    t = int(input())

    dct = {'{': '}', '(': ')', '[': ']'}
    for t_itr in range(t):
        print()
        expression = input()
        symbols = [i for i in expression]
        stack = [symbols[0]]
        symbols.pop(0)
        for symbol in symbols:
            if len(stack) == 0:
                stack.append(symbol)
            elif stack[-1] in dct:
                if dct[stack[-1]] == symbol:
                    stack.pop()
                else:
                    stack.append(symbol)
            else:
                stack.append(symbol)
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')
