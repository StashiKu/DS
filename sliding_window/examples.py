# O(n) solution for finding
# maximum sum of a subarray of size k

def maxSum(arr, k):
    n = len(arr)

    if n < k:
        print("Invalid")
        return -1

    window_sum = sum(arr[:k])

    max_sum = window_sum

    end = n - k

    for i in range(end):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(window_sum, max_sum)

    return max_sum


# Driver code
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
print(maxSum(arr, k))

# [1, 4, 2, 10, 2, 3, 1, 0, 20]
# 4
# window_sum =24
# max_sum = 24
# i = 4
