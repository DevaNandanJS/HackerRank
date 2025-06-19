/*
Problem: Time Conversion
Difficulty: Unknown
URL: https://www.hackerrank.com/challenges/one-week-preparation-kit-time-conversion/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one
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
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    sp = s.split(':')
    if "A" in sp[2]:
        sp[2] = sp[2].replace("AM","")
        if sp[0]=="12":
            sp[0]="00"
    else:
        sp[2] = sp[2].replace("PM","")
        if sp[0]=="12":
            sp[0]="12"
        else:
            sp[0]=str(int(sp[0])+12)
    return ":".join(sp)
    
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
