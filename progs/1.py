# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

if __name__ == "__main__":
    july_sales = [
        (random.randint(100, 1000), 
        random.randint(100, 1000)) for _ in range(31)
    ]
    august_sales = [
        (random.randint(100, 1000), 
        random.randint(100, 1000)) for _ in range(31)
    ]
    res = (
        sum([sum(i) for i in july_sales]) + 
        sum([sum(i) for i in august_sales])
    )
    print(f"Sum of sales in July and August = {res}")
