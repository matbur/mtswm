#!/usr/bin/env python

import numpy as np
from scipy.optimize import minimize


def foo(t, k, v):
    return (1 - np.exp(-k * t)) / (k * v)


def error(x):
    k, v = x
    t = np.array([10., 30., 120.], dtype=np.float128)
    c = np.array([.0019, .0052, .014], dtype=np.float128)
    f = foo(t, k, v)
    print(f)
    err = np.sum((f - c) ** 2)
    return err


def main():
    res = minimize(
        error,
        np.array([1, 1]),
        method='L-BFGS-B',
        options={
            'maxls': 100,
        }
    )
    print(res)


if __name__ == '__main__':
    # main()
    print(error([.01, 5000]))
