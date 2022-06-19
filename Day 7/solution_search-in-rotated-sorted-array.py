from typing import List


class Solution:
    """
    problem statement : https://leetcode.com/problems/search-in-rotated-sorted-array/
    Understanding Solution link: https://www.tutorialspoint.com/search-in-rotated-sorted-array-in-python
    Algorithm:
    >> low := 0 and high := length of array
    >> while low < high
        >> find mid as mid := low + (high - low)/2
        >> if arr[mid] = target, then return mid
        >> if arr[low] <= arr[mid]
            >> if target >= arr[low] and target < arr[mid], then high := mid, otherwise low := mid + 1
        >> otherwise
            >> if target <= arr[high - 1] and target > arr[mid], then low := mid + 1, otherwise high := mid
    >>return -1
    """

    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:
                if target >= nums[low] and target < nums[mid]:
                    high = mid
                else:
                    low = mid + 1
            else:
                if target <= nums[high - 1] and target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid
        return -1


if __name__ == "__main__":
    print(Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
