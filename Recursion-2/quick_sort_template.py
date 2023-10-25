# Quick Sort Algorithm
"""
In detail, given a list of values to sort, the quick sort algorithm works in the following steps:

    1. First, it selects a value from the list, which serves as a pivot value to divide the list into two sublists.
       One sublist contains all the values that are less than the pivot value,
       while the other sublist contains the values that are greater than or equal to the pivot value.
       This process is also called partitioning. The strategy of choosing a pivot value can vary.
       Typically, one can choose the first element in the list as the pivot, or randomly pick an element from the list.

    2. After the partitioning process, the original list is then reduced into two smaller sublists. We then recursively sort the two sublists.

    3. After the partitioning process, we are sure that all elements in one sublist are less or equal than any element in another sublist.
       Therefore, we can simply concatenate the two sorted sublists that we obtain in step [2] to obtain the final sorted list. 
       The base cases of the recursion in step [2] are either when the input list is empty or contains only a single element.
       In either case, the input list can be considered as sorted already.

As one can see, the essential idea of the quick sort algorithm is the partitioning process, 
which elegantly reduces the problems into smaller scale and meanwhile moves towards the final solution,
i.e. after each partitioning, the overall values become more ordered. 
"""

def quicksort(arr: list) -> list:
    """
    Sorts an array in the ascending order in O(n log n) time
    :param arr: a list of numbers
    :return: the sorted list
    """
    n = len(arr)
    qsort(arr, 0, n - 1)

def qsort(arr: list, l: int, r: int) -> list:
    """
    Helper
    :param arr: the list to sort
    :param l:  the index of the first element in the list
    :param r:  the index of the last element in the list
    :return: the sorted list
    """
    if l < r:
        p = partition(arr, l, r)
        qsort(arr, l, p - 1)
        qsort(arr, p + 1, r)

def partition(arr: list, l: int, r: int) -> int:
    """
    Picks the last element r as a pivot
     and returns the index of pivot value in the sorted array
    """
    pivot = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[j] = arr[j], arr[i]
    return i