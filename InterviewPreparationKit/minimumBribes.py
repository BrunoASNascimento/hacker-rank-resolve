#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#


def minimumBribes(q):
    bribes = 0
    for i in range(len(q)-1, -1, -1):  # Start from the last person in the queue
        if q[i] - (i + 1) > 2:  # Check if the current person has bribed more than 2 people
            print("Too chaotic")
            return
        # Only need to check the positions one or two ahead of where they originally should be
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1

    print(bribes)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
