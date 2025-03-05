import time
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

sizes = [1000, 2000, 4000, 8000]
array_times = []
linked_list_times = []

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def binary_search(self, num):
        # Convert linked list to an array (O(n) time)
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        
        # Perform binary search on the array (O(log n) time)
        left, right = 0, len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            if values[mid] == num:
                return True
            elif values[mid] < num:
                left = mid + 1
            else:
                right = mid - 1
        return False

class Array:
    def __init__(self):
        self.data = []
    
    def append(self, value):
        self.data.append(value)
    
    def binary_search(self, num):
        left, right = 0, len(self.data) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.data[mid] == num:
                return True
            elif self.data[mid] < num:
                left = mid + 1
            else:
                right = mid - 1
        return False

# Performance Measurement
for size in sizes:
    data = sorted(random.sample(range(size * 10), size))
    target = data[size // 2]  # Middle element
    
    # Measure array binary search time
    arr = Array()
    for num in data:
        arr.append(num)
    
    start = time.perf_counter()
    arr.binary_search(target)
    array_times.append(time.perf_counter() - start)
    
    # Measure linked list binary search time
    ll = LinkedList()
    for num in data:
        ll.append(num)
    
    start = time.perf_counter()
    ll.binary_search(target)
    linked_list_times.append(time.perf_counter() - start)

# Interpolation with safeguard
if len(sizes) > 1:
    sizes_np = np.array(sizes)
    array_interp = interp1d(sizes_np, array_times, kind='quadratic')
    linked_list_interp = interp1d(sizes_np, linked_list_times, kind='quadratic')

# Plot results
plt.figure(figsize=(8, 5))
plt.plot(sizes, array_times, 'bo-', label='Array Binary Search')
plt.plot(sizes, linked_list_times, 'ro-', label='Linked List Binary Search')

if len(sizes) > 1:  # Avoid interpolation if not enough data points
    plt.plot(sizes, array_interp(sizes_np), 'b--', alpha=0.6)
    plt.plot(sizes, linked_list_interp(sizes_np), 'r--', alpha=0.6)

plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Binary Search Performance: Array vs Linked List')
plt.legend()
plt.show()

'''
Upon seeing the graph results, it confirms our pre-existing knowledge that the
random access binary search of arrays is on average O(1) whereas it is O(n) in linked lists. The reason for this is because the binary search for the linked list
to an array before it begins searching, because of this conversation, the complecity increases to O(n). This makes the overall
complexity of linked list binary search into O(nlogn) whereas the overal complexity for array binary search is
O(logn) which is much more efficient.

In essence. We know that Linked lists have a random access complexity of O(n) unlike arrays which have a random access complexity of O(1).
Given that the binary search itzelf has a complexity of O(log(n)); in conjuction with linked lists, the overall complexity becomes O(n) * O(log(n)) which is  O(nlog(n))
'''