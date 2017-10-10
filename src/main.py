#!/usr/bin/env python

import numpy as np


def foo(t, k, v):
    return (1 - np.exp(-k * t)) / (k * v)
    # return t * k + v


def main():
    q = 1
    t = np.array([10., 30., 120.], dtype=np.float128)
    c = np.array([.0019, .0052, .014], dtype=np.float128)

    all_k = np.linspace(.01002009, .01002010, 1 << 11, dtype=np.float128)
    all_v = np.linspace(4986.51, 4986.525, 1 << 13, dtype=np.float128)
    # l = [-1, 1]

    ans = (10 ** 10, -1, -1)

    for k in all_k:
        for v in all_v:
            f = foo(t, k, v)
            temp = np.sum((f - c) ** 2), k, v
            # print(temp)
            if temp < ans:
                ans = temp
                print(ans)

    print()
    for i in ans:
        print(f'{i:.100f}')
    print(ans)


if __name__ == '__main__':
    # main()
    k, v = (0.010020095109916951973, 4986.5215040898547159)
    t = np.array([10., 30., 120.], dtype=np.float128)
    for i in t:
        f = foo(i, k, v)
        print(i, np.round(f, 4))
