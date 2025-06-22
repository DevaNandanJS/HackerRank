/*
Problem: String Split and Join
Difficulty: Unknown
URL: https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true
Language: python
Date: 2025-06-22
*/

def split_and_join(line):
    m = line.split(" ")
    n = '-'.join(m)
    return n

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)