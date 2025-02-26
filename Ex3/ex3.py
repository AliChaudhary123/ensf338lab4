# ENSF 338
# Lab 4
# Exercise 3

# The growth factor is 4
# Reference: line 65

import sys

arr = []
prev_capacity = sys.getsizeof(arr)

for i in range(65):
    arr.append(None)
    print(sys.getsizeof(arr))
