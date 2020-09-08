#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.


def jumpingOnClouds(c):
    print(c)
    control = 0
    jump_count = 0
    for i in range(len(c)):
        print(control)

        while control < len(c)-1:
            print(control)
            try:
                if (c[control+2] == 0) or (c[control+1] == 1):
                    control += 2
                    jump_count += 1
                else:
                    control += 1
                    jump_count += 1
            except:
                control += 1
                jump_count += 1

    print(f'Jump: {jump_count}')
    return jump_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    fptr.write(str(result) + '\n')
    fptr.close()
