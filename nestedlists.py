"""
https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
"""

from collections import defaultdict

d = defaultdict(list)
t1 = [('Harry', 37.5), ('Barry', 37.5), ('Larry', 25.0), ('Lisa', 33.0)]

for x, y in t1:
    d[y] = d[y] + x

print(d)

