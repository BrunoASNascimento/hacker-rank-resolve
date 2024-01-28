#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    # Write your code here
    index_value = 0
    min_sum = sum(arr)
    max_sum = 0
    for index_value in range(len(arr)):
        sum_arr = sum(arr[:index_value] + arr[index_value+1:])
        if sum_arr < min_sum:
            min_sum = sum_arr
        if sum_arr > max_sum:
            max_sum = sum_arr

    print(min_sum, max_sum)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
