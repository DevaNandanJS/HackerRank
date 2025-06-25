/*
Problem: Capitalize!
Difficulty: Unknown
URL: https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true
Language: python
Date: 2025-06-25
*/

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    a = s.split()
    result = []
    for i in a:
        if len(i)>0:
            result.append(i[0].upper()+i[1:].lower())
    d = " ".join(result)   
    return d
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
