from typing import List


class BruteForceApproachSolution:
    """
    Problem statement : https://leetcode.com/problems/maximum-product-subarray
    https://www.interviewbit.com/blog/maximum-product-subarray-problem/
    A simple approach to solve this problem is to find all possible subarrays of the given input array
    and maximize the product of all subarrays found so far.
    `Algorithm steps:`
    >> Initialise a variable result = A[0]  to store the maximum product.
    >> Run two nested loops from i = 0 till N – 1 and j  from i + 1 till N and for each subarray A[i….j],
        find the product of the subarray.
    >> Update and maximize result.

    Time Complexity: O(N^2), where N is total size of the array
    Space Complexity: O(1), as no extra space is used
    """

    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        result = nums[0]

        for i in range(len(nums)):
            accu = 1
            for j in range(i, len(nums)):
                accu *= nums[j]
                result = max(result, accu)
        return result


class Solution:
    """
    Problem statement : https://leetcode.com/problems/maximum-product-subarray
    https://www.interviewbit.com/blog/maximum-product-subarray-problem/
    Dynamic Programming approach : If we observe clearly, the maximum product will always lie either from the starting of the array
        or from the end of the array.
    `Algorithm steps:`
    >> Initialise a variable result = A[0]  to store the maximum product.
    >> Initialise two variables max_so_far and min_so_far with A[0], which stores the maximum and minimum product obtained so far
    >> Traverse the input array and for negative element swap max_so_far and min_so_far.
    >> Maximize max_so_far and update it with max_so_far * A[i]
    >> Minimise min_so_far and update it with min_so_far * A[i]
    >> Update result with maximum of max_so_far and min_so_far.
    >> Return result.

    Time Complexity: O(N), where N is total size of the array
    Space Complexity: O(1), as no extra space is used
    """

    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far

        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)
            max_so_far = temp_max
            result = max(max_so_far, result)
        return result


if __name__ == "__main__":
    print(BruteForceApproachSolution().maxProduct([2, 3, -2, 4]))
    print(BruteForceApproachSolution().maxProduct([-2, 0, -1]))
    print(Solution().maxProduct([2, 3, -2, 4]))
    print(Solution().maxProduct([-2, 0, -1]))
