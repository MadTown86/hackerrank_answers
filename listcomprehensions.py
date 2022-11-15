"""
https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true
"""
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    bx, yx, zx, bn = 0, 0, 0, 0
    c = []

    res = [[i, j, k] for i in [x for x in range(x+1)] for j in [y for y in range(y+1)] for k in [z for z in range(z+1)] if (i+j+k) != n]
    print(res)