#!/bin/python3

import math
import os
import random
import re
import sys
import collections

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#


def birthdayCakeCandles(candles):
    # Write your code here
    data = collections.Counter(candles)
    max_number = data[max(candles)]
    # print(data[max(candles)])
    return max_number


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    # fptr.write(str(result) + '\n')

    # fptr.close()
