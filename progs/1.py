# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

if __name__ == "__main__":
    julySales = [
        (random.randint(100, 1000) for i in range(31)),
        (random.randint(100, 1000) for i in range(31))
    ]
    augustSales = [
        (random.randint(100, 1000) for i in range(31)),
        (random.randint(100, 1000) for i in range(31))
    ]
    res = (
        sum(julySales[0])
        + sum(julySales[1])
        + sum(augustSales[0])
        + sum(augustSales[1])
    )
    print(f"Sum of sales in July and August = {res}")
