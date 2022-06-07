from typing import List


class Solution:
    """
    Problem statement : https://leetcode.com/problems/missing-number/
    """

    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums) + 1):
            if i not in nums:
                return i


if __name__ == "__main__":
    print(Solution().missingNumber([3, 0, 1]))
    print(Solution().missingNumber([0, 1]))
    print(Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
