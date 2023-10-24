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