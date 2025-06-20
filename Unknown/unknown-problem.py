/*
Problem: unknown-problem
Difficulty: Unknown
URL: https://www.hackerrank.com/test/eoipgdk427n/questions/a8taf02a12a
Language: python
Date: 2025-06-20
*/

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    n = len(arr)
    arr.sort()
    median = arr[n//2]
    return median
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
