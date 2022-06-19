from collections import defaultdict
from typing import List


class Solution:
    """
    problem statement : https://leetcode.com/problems/subarray-sum-equals-k/
    Understanding Solution Link : https://www.interviewbit.com/blog/subarray-sum-equals-k/
    We can solve this problem in linear time complexity using a hashmap-based approach. The algorithm is described as follows:
    >> Traverse the array, and keep track of the current running sum up to the ith index in a variable, say sum.
    >> Also, hash the different values of the sum obtained so far, into a hashmap.
    >> If the sum equals k  at any point in the array, increment the count of subarrays by 1.
    >> If this value of sum has exceeded k by a value of sum – k, we can find the number of subarrays,
        found so far with sum = sum – k, from our hashmap. Observe that if these subarrays are deleted from our current array,
        we will again obtain a sum of k. So, we add to our answer, the number of subarrays with sum = sum – k found so far from our hashmap.
    >> After traversing through the entire array once and applying the above steps, return the calculated result.
    Time Complexity: O(n) & Space Complexity: O(1)
    """

    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # To Understand default dict : https://www.geeksforgeeks.org/defaultdict-in-python/
        # default dict in sub-class of dictionary class . does raise keyError in absent of Key . return default value
        hash_map = defaultdict(lambda: 0)
        count = 0
        summation = 0
        for i in range(n):
            summation += nums[i]
            if summation == k:
                count += 1
            if (summation - k) in hash_map:
                count += hash_map[summation - k]
            hash_map[summation] += 1
        return count


if __name__ == "__main__":
    print(Solution().subarraySum(nums=[1, 1, 1], k=2))
