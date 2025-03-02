1. Compare advantages and disadvantages of arrays vs linked list
(complexity of task completion)
Arrays are physically ordered and structured lists. Arrays allow for quick indexing, if the location is known. This time complexity is O(1). This way, replacements and retrievals are quick, because the position is known. For disadvantages, arrays impose maximum size for lists, meaning arrays are fixed and dynamic. For fixed arrays, a disadvantage could be that memory could be waasted, as the array only needs a few elements. If we want to expand the size of a dynamic array, this requires copying into temporary arrays, which allocates memory. Regarding linked lists, they are resizable without penalty like dynamic arrays. This means we can expand on the go, by adding new nodes to the linked lists. The disadvantage is that it is no longer indexable, meaning we must sequentially traverse through the linked list to find a key. 

2. For arrays, we are interested in implementing a replace function that acts as a deletion followed by insertion.
How can this function
be implemented to minimize the impact of each of the standalone
tasks?
To implement a replace function regarding arrays, if the key is at the end of an array, we can delete this value and insert at the end with a complexity O(1), as deleting the last element in an array doesn't cause it to shift left and inserting at the end doesn't shift any elements to the right. In other cases, we need to find the index of the value we want to replace and handle deletion followed by insertion in one function. This causes this step to be done more efficiently, as it is all in one function. 

3. Assuming you are tasked to implement a doubly linked list with a
sort function, given the list of sort functions below, state the
feasibility of using each one of them and elaborate why is it possible
or not to use them.

1. Insertion sort

In a doubly linked list, insertion sort can be used, as we can traverse forwards or backwards to insert elements to their positions. One way to implement this is through an in-place insertion sort, which directly modifies the list by rearranging its nodes, using two pointers to track the sorted and unsorted portions. While insertion sort is possible, it is not the most efficient approach, as the time complexity for swapping elements is O(n²). This cost increases as the size of the list grows.


2. Merge sort
Merge sort can also be used in a doubly linked list. This sort is more efficient because it implements a divide and conquer approach, which is more efficient in the performance. Merge sort is better suited for larger data, due to the time complexity being O(n log n). In a doubly linked list, splitting the linked list is more complicated than insertion sort due to the next and previous pointers, as well as using recursion to sort these lists. 


4. Also show the expected complexity for each and how it differs from
applying it to a regular array. 

Insertion sort in a doubly linked list has a time complexity of O(n^2) and merge sort has a time complexity of O(n log n). Compared to a regular array, insertion sort in the average case has complexity O(n^2) and insertion sort has complexity of O(n log n). 
