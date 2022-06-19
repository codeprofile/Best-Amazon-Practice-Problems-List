from typing import List


class Solution:
    """
    problem statement : https://leetcode.com/problems/maximum-sum-circular-subarray/
    Understanding Solution Link: https://www.geeksforgeeks.org/maximum-contiguous-circular-sum/
    Approach:modified  Kadane’s algorithm to find a minimum contiguous subarray sum and the maximum contiguous subarray sum,
            then check for the maximum value between the max_value and the value left after subtracting min_value from the total sum.
    Algorithm :
    >> We will calculate the total sum of the given array.
    >> We will declare the variable curr_max, max_so_far, curr_min, min_so_far as the first value of the array.
    >> Now we will use Kadane’s Algorithm to find the maximum subarray sum and minimum subarray sum.
    >> Check for all the values in the array:-
        >> If min_so_far is equaled to sum, i.e. all values are negative, then we return max_so_far.
        >> Else, we will calculate the maximum value of max_so_far and (sum – min_so_far) and return it.
    """
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        # Corner Case
        if n == 1:
            return nums[0]

        # Initialize sum variable which
        # store total sum of the array.
        sum = 0

        for i in range(n):
            sum += nums[i]

        # Initialize every variable
        # with first value of array.
        curr_max = nums[0]
        max_so_far = nums[0]
        curr_min = nums[0]
        min_so_far = nums[0]

        # Concept of Kadane's Algorithm
        for i in range(1, n):
            # Kadane's Algorithm to find Maximum subarray sum.
            curr_max = max(curr_max + nums[i], nums[i])
            max_so_far = max(max_so_far, curr_max)

            # Kadane's Algorithm to find Minimum subarray sum.
            curr_min = min(curr_min + nums[i], nums[i])
            min_so_far = min(min_so_far, curr_min)

        if min_so_far == sum:
            return max_so_far

        # returning the maximum value
        return max(max_so_far, sum - min_so_far)


if __name__ == "__main__":
    print(Solution().maxSubarraySumCircular(nums=[1,-2,3,-2]))





