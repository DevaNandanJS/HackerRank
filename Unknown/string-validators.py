/*
Problem: String Validators
Difficulty: Unknown
URL: https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true
Language: python
Date: 2025-06-23
*/

if __name__ == '__main__':
    s = input()
    a=b=c=d=e= False
    for char in s:
        if char.isalnum():
            a = True
        if char.isalpha():
            b = True
        if char.isdigit():
            c = True
        if char.islower():
            d = True
        if char.isupper():
            e = True
    print(a,b,c,d,e, sep ='\n')
        
    
