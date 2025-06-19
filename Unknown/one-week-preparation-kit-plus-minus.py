/*
Problem: Plus Minus
Difficulty: Unknown
URL: https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one
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
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    p = 0
    neg = 0
    z = 0
    
    for i in arr:
        if i>0:
            p+= 1
        elif i<0:
            neg+= 1
        else:
            z+=1
    print (p/n)
    print (neg/n)
    print (z/n)
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
    
