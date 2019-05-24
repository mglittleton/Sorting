# STRETCH: implement Linear Search
def linear_search(arr, target):
    # TO-DO: add missing code
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1

    # TO-DO: add missing code
    while high - low > -1:
        mid = round((high + low) / 2)
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):
    if not len(arr):
        return -1

    middle = (low+high)//2
    print(low, high, arr[middle])

    if high - low == 0:
        if arr[middle] == target:
            return middle
        else:
            return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
    if arr[middle] == target:
        return middle
    elif arr[middle] > target:
        high = middle - 1
    else:
        low = middle + 1

    return binary_search_recursive(arr, target, low, high)


