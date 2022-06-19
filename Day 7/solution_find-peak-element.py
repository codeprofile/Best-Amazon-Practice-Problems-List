from typing import List


class Solution:
    """
    problem statement : https://leetcode.com/problems/find-peak-element/
    self-written solution with linear time complexity O(n)
    """

    def findPeakElement(self, nums: List[int]) -> int:
        # Initialising maximum to first element in the list
        maxima = nums[0]
        output = 0
        for i in range(1, len(nums[1:]) + 1):
            if nums[i] > maxima:
                maxima = nums[i]
                output = i
        return output


if __name__ == "__main__":
    print(Solution().findPeakElement(nums=[1,2]))