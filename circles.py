#!/usr/bin/env python3

import numpy as np

N = int(input())

def whack(A, B):
    a0, a1, b0, b1 = A[0], A[1], B[0], B[1]

    def between(a, b, c):
        return a < b < c
    def four(a, b, c, d):
        return a < b < c < d

    if between(a0, b0, a1) and between(a0, b1, a1): return False
    if between(a0, a1, b0) and between(a0, a1, b1): return False
    if between(b0, a0, a1) and between(b1, a0, a1): return False

    if four(b0, a0, a1, b1): return False
    if four(b1, a0, a1, b0): return False

    return True


def main(lim):
    smash = list(map(int, input().split()))
    locations = [[] for _ in range(lim + 1)]
    arrcross = [[1 if i == j else 0 for i in range(lim + 1)] for j in range(lim + 1)]
    for loc in range(lim * 2):
        i = smash[loc]
        locations[i].append(loc)
    for a in range(1, len(locations)):
        for b in range(a + 1, len(locations)):
            A, B = locations[a], locations[b]
            if whack(A,B):
                arrcross[a][b] = 1
                arrcross[b][a] = 1
    s = []
    for i in range(lim + 1):
        s.append(sum(map(lambda x: x[i], arrcross)))
    # print(arrcross)
    # print(s)
    c = 0
    for i in range(1, lim + 1):
        if s[i] >= 3:
            c += 1
            if c >= 3:
                return 'no'
    if c >= 3:
        return 'no'
    return 'yes'

for _ in range(N):
    lim = int(input())
    print(main(lim))
