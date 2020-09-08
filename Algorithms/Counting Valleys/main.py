#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.


def countingValleys(n, s):
    print(n, s)
    count_u = 0
    count_d = 0
    valleys = 0
    control_sea = 0
    control = []
    for i in range(0, len(s)):
        if s[i] == 'U':
            control_sea += 1
        else:
            control_sea -= 1
        control.append(control_sea)
        if ((control[i-1] == 0) and (control[i] < 0)) or ((i == 0) and (control[i] < 0)):
            valleys += 1
        print(control_sea)
    print(valleys)
    return (valleys)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    s = input()
    result = countingValleys(n, s)
    fptr.write(str(result) + '\n')
    fptr.close()
