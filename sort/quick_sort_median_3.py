def quicksort(arr, low, high):
    if low < high:
        # Choose the pivot using Median-of-three approach
        pivot_index = median(arr, low, high)

        # Partition the array and get the new pivot index
        new_pivot_index = partition(arr, low, high, pivot_index)

        # Recursively sort the two sub-arrays
        quicksort(arr, low, new_pivot_index - 1)
        quicksort(arr, new_pivot_index + 1, high)


def median(arr, low, high):
    mid = (low + high) // 2

    if arr[low] <= arr[mid]:
        if arr[mid] <= arr[high]:
            return  mid

    else:
        if arr[low] <= arr[high]:
            return low

    return high


def partition(arr, low, high, pivot_index):
    pivot_value = arr[pivot_index]

    # Move the pivot to the end of the sub-array
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    i = low
    for j in range(low, high):
        if arr[j] < pivot_value:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    # Move the pivot to its final sorted position
    arr[i], arr[high] = arr[high], arr[i]

    return i


arr = [1, 5, 2, 7, 3, 8, 9]
# [5, 2, 3, 1, 9, 8, 7]
# pivotIndex = 3
# pivotValue = 7
# i =4
# j = 5
# return 2
quicksort(arr, 0, len(arr) - 1)
print(arr)