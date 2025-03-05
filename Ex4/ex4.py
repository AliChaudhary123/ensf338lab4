# ENSF 338
# Lab 4
# Exercise 4

# Best case: O(n)
# If all elements of li are less than 5, all elements of the array will be iterated over once.

# Worst case: O(n^2)
# If all elements of li are greater than 5, all elements of the array will be iterated over once
# for each array element resulting in a complexity of O(n^2).

# Average case: O(n^2)
# Some elements are greater than 5 and some are not. For every element greater than 5, the array
# will be iterated over, so ultimately the time for the code to complete scales quadratically
# with the input.

import timeit
import matplotlib.pyplot as plt

# Modified version:
def processdata(li):
    for i in range(len(li)):
        if li[i] > 5:
            for j in range(len(li)):
                li[j] = 2

# Searching in a sorted array

# Inefficient implementaion:
# Worst case: O(n)
def linear_search(item, data):
    for i in range(0, len(data)):
        if data[i] == item:
            return i
    return -1


# Efficient implementation
# Worst case: O(logn)
def binary_search(item, data):
    lower = 0
    upper = len(data) - 1

    while lower <= upper:
        mid = lower + (upper - lower) // 2

        if data[mid] == item:
            return mid
        elif data[mid] > item:
            upper = mid - 1
        else:
            lower = mid + 1

    return -1

# Time and plot distribution
lin_times = []
bin_times = []

data = [x for x in range(10000)]

lin_times = timeit.repeat(lambda: linear_search(999, data), number=100, repeat=500)
bin_times = timeit.repeat(lambda: binary_search(999, data), number=100, repeat=500)

plt.hist(lin_times, color="red", label="linear search")
plt.hist(bin_times, color="green", label="binary search")
plt.legend(loc="upper right")
plt.show()
