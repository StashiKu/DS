# Example 1:
#
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
# Example 2:
#
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
# Example 3:
#
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].


# slow solution
def twoSum(numbers, target):
    res = []
    n = len(numbers)

    for i in range(0, n):
        if len(res):
            return res
        j = i + 1
        while j < n:
            if numbers[i] + numbers[j] == target:
                res = [i+ 1, j + 1]
                break
            j += 1
    return res

print(twoSum([2,7,11,15], 9))


# var twoSum = function(numbers, target) {
#     const seen = {};
#     for (let i = 0; i < numbers.length; i++) {
#         const needed = seen[target - numbers[i]];
#         if (needed !== undefined) {
#             return [needed + 1, i + 1];
#         }
#         seen[numbers[i]] = i;
#     }
# };

# var twoSum = function (numbers, target) {
#   let left = 0,
#     right = numbers.length - 1;
#
#   while (left < right) {
#     const currentSum = numbers[left] + numbers[right];
#     if (currentSum === target) {
#       return [left+1, right+1];
#     }
#     if (target < currentSum) {
#       right--;
#     } else if (target > currentSum) {
#       left++;
#     }
#   }
# };