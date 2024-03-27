# Python program to find maximum contiguous subarray

# Function to find the maximum contiguous subarray
from sys import maxint
from sys import maxsize

def maxSubArraySum(a, size):
	max_so_far = -maxint - 1
	max_ending_here = 0

	for i in range(0, size):
		max_ending_here = max_ending_here + a[i]
		if (max_so_far < max_ending_here):
			max_so_far = max_ending_here

		if max_ending_here < 0:
			max_ending_here = 0
	return max_so_far

a = [-2, -3, 4, -1, -2, 1, 5, -3]

print("Maximum contiguous sum is", maxSubArraySum(a, len(a)))

# [-2, -3, 4, -1, -2, 1, 5, -3]
# max_ending = 4
# max_so_far = 7
# i = 7



# Function to find the maximum contiguous subarray
# and print its starting and end index
def maxSubArraySum(a, size):

	max_so_far = -maxsize - 1
	max_ending_here = 0
	start = 0
	end = 0
	s = 0

	for i in range(0, size):

		max_ending_here += a[i]

		if max_so_far < max_ending_here:
			max_so_far = max_ending_here
			start = s
			end = i

		if max_ending_here < 0:
			max_ending_here = 0
			s = i+1

	print("Maximum contiguous sum is %d" % (max_so_far))
	print("Starting Index %d" % (start))
	print("Ending Index %d" % (end))

a = [-2, -3, 4, -1, -2, 1, 5, -3]
maxSubArraySum(a, len(a))

# [-2, -3, 4, -1, -2, 1, 5, -3]
# max_so_far = 7
# curr_max = 4
# i = 7
# start = 2
# end = 6
# s = 2


# Python program for the above approach
def max_sub_array_sum(a, size):
	dp = [0] * size
	dp[0] = a[0]
	ans = dp[0]
	for i in range(1, size):
		dp[i] = max(a[i], a[i] + dp[i - 1])

		ans = max(ans, dp[i])
	print(ans)
if __name__ == "__main__":
	a = [-2, -3, 4, -1, -2, 1, 5, -3]
	n = len(a)
	max_sub_array_sum(a, n)

# [-2, -3, 4, -1, -2, 1, 5, -3]
# dp = [-2, -3, 4, 3, 1, 2, 7, 4] // -3/4
# i = 7
# answer = 7




