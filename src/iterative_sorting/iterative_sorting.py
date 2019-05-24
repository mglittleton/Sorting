import random
# TO-DO: Complete the selection_sort() function below
def selection_sort( arr ):
    # loop through n-1 elements

    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        # TO-DO: swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp
        smallest_index = j

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swap = 1
    while swap > 0:
        swap = 0
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                swap += 1
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    if not len(arr):
        return arr
    lowNum = arr[0]
    highNum = arr[0]
    for i in arr:
        if i < lowNum:
            lowNum = i
        elif i > highNum:
            highNum = i
    placeList = [0 for i in range(lowNum, highNum + 1)]
    for i in arr:
        placeList[i - lowNum] += 1
    for i in range(1, len(placeList)):
        placeList[i] += placeList[i - 1]
    placeList = [i - 1 for i in placeList]
    newList = [i for i in arr]
    for i in newList:
        arr[placeList[i - lowNum]] = i
        placeList[i - lowNum] -= 1
    return arr

