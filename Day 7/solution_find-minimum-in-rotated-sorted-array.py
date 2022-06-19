from typing import List


class Solution:
    """
    problem statement : https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
    Understanding solution video : https://www.youtube.com/watch?v=nIVW4P8b1VA
    Binary search is used as it takes o(log n)
    """

    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # already sorted array
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            # already unsorted array will start calculating mid value
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res


if __name__ == "__main__":
    print(Solution().findMin(nums=[3, 4, 5, 1, 2]))
