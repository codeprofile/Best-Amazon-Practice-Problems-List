from typing import List


class Solution:
    """
    Problem statement : https://leetcode.com/problems/two-sum/
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Iterating through the nums array
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # checking if ith index element addition with all jth index element
                if nums[i] + nums[j] == target:
                    return [i, j]


if __name__ == "__main__":
    print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))
    print(Solution().twoSum(nums=[3, 2, 4], target=6))
    print(Solution().twoSum(nums=[3, 3], target=6))
