/*
Problem: Mini-Max Sum
Difficulty: Unknown
URL: https://www.hackerrank.com/interview/preparation-kits/one-week-preparation-kit/one-week-day-one/challenges
Language: python
Date: 2025-06-19
*/

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
    arr.sort(reverse=True)
    minn = sum(arr[1::])
    maxx = sum(arr[:len(arr)-1:])
    print(minn,maxx)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
