#!/bin/python3

import math
import os
import random
import re
import sys

def decode(mat,m):
    """
    """
    code = ['' for j in range(m)]
    for v in mat:
        for i in range(m):
            code[i] += v[i]
       
    decoded = re.sub(r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])',' ',''.join(code))
    print(decoded)
    


nm = input().split()

n = int(nm[0])

m = int(nm[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
decode(matrix,m)
