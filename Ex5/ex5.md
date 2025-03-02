
1. These approaches are designed to deal with different types of
measurement noise. Think about what happens when we try to time
a program, and which types of issues may result in an incorrect
measurement. Reflect on how the two approaches (timeit and
repeat) attempt to address these issues. Discuss when it is
appropriate to use one or the other.


It is appropriate use the timeit function when the reduntant steps are needed to be removed. The purpose of this function is to accurately measure the execution time of the code. This approach attempts to address the problem by running it many amount of times, in an attempt to reduce the redundancies that can happen when trying to time code because it tries to "average out" the time over multiple executions. 


The repeat function is used and is repeated multiple times, and returns the total execution time in an array format. Timeit.timeit essentially is implemented to create a more efficient runtime for execution. This repeat function will return a list of 5 different execution times after a piece of code is run 10 times. 



2. Typically, the output of timeit is post-processed to compute some
sort of aggregate statistics. Let’s only consider three: average, min,
and max. Which one is the appropriate statistic to apply to the output
of timeit.timeit()? What is the appropriate statistics to apply
to the output of timeit.repeat()


For timeit.timeit(), the best statistics is avg, which is the average time. Since this method returns a total time for all the executions, this can be regarded as the average time, which is total time divided by the number of executions. 

For timeit.repeat(), the best statistic is all min. max and average. Since the repeat function is repeated multiple times, this may include all possible results, including the longest, shortest, and average. 

