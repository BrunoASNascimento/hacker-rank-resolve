#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.


def repeatedString(s, n):
    if len(s) == 1 and s == 'a':
        return int(n)
    elif ((len(s) == 1) and (s != 'a')) or (s.count('a') == 0):
        return int(0)
    elif len(s) >= n:
        return int(s[:int(n)].count('a'))
    else:
        control_constructor = int(n//len(s))
        return(s.count('a')*control_constructor+s[:int(n % control_constructor)].count('a'))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    n = int(input())
    result = repeatedString(s, n)
    fptr.write(str(result) + '\n')
    fptr.close()
