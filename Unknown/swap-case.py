/*
Problem: sWAP cASE
Difficulty: Unknown
URL: https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
Language: python
Date: 2025-06-23
*/

def swap_case(s):
    b= ""
    for char in s:
        a = " "
        if char == char.upper():
            a = char.lower()
        if char == char.lower():
            a = char.upper()
        b = b+a
    return b

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)