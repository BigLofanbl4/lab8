# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

if __name__ == "__main__":
    july_sales = [
        (random.randint(100, 1000) for i in range(31)),
        (random.randint(100, 1000) for i in range(31))
    ]
    august_sales = [
        (random.randint(100, 1000) for i in range(31)),
        (random.randint(100, 1000) for i in range(31))
    ]
    res = (
        sum(july_sales[0])
        + sum(july_sales[1])
        + sum(august_sales[0])
        + sum(august_sales[1])
    )
    print(f"Sum of sales in July and August = {res}")
