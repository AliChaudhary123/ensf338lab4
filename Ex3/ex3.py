# ENSF 338
# Lab 4
# Exercise 3

# The growth factor is 1.125. Each time the amount of new elements exceeds the array size the array is grown
# by (9/8) + 6 of its original size. Padding is added to mak ethe new size a multiple of 4.
# Reference: lines 60 - 68

import timeit
import sys
import matplotlib.pyplot as plt

arr = []
prev_cap = sys.getsizeof(arr)

for i in range(64):
    arr.append(7)
    curr_cap = sys.getsizeof(arr)
    if curr_cap != prev_cap:
        print("Size: ", i + 1, "| Capacity: ", curr_cap // 4)
        prev_cap = curr_cap

# S = 52
# For S to S + 1
avg_times1 = []
for i in range(100):
    arr = [7] * 52
    avg_times1.append(timeit.timeit(lambda: arr.append(7), number=1))

print(len(arr))
print()

# For S - 1 to S
avg_times2 = []
for i in range(100):
    arr = [7] * 51
    avg_times2.append(timeit.timeit(lambda: arr.append(7), number=1))

print(len(arr))

plt.hist(avg_times1, label="S + 1")
plt.hist(avg_times2, label="S - 1", alpha=0.5)
plt.legend(loc="upper right")
plt.show()

# The histograms suggest that growing the array from S - 1 to S is faster and has a more consistent time.
# This makes sense as when growing from S - 1 to S, capacity does not need to be increased. The S to S + 1
# times are more inconsistent and are usually slower. This makes sense as in this situation the array's
# capacity must be increased.
