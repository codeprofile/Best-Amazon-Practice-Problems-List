from typing import List


class Solution:
    """
    Problem statement : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
    Below code is using two pointer technique : here left_index and right_index are the pointers
    """

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_index = 0  # left_index is a left pointer  starts with 0 index
        right_index = len(numbers) - 1  # right_index is a right pointer starts with last index
        while left_index < right_index:
            # if summation of left index element and right element is less than target given
            # then left index is moved with 1 because i moving forward value increases (sorted array in ascending order)
            if numbers[left_index] + numbers[right_index] < target:
                left_index += 1
            elif numbers[left_index] + numbers[right_index] > target:
                # if summation of left index element and right element is greater than target given then right index
                # is moved with 1  because i moving forward value decreases the value as we are parsing array in
                # reverse order here
                right_index -= 1
            else:
                # As Indexing should be 1-indexed so added one to the final index
                return [left_index + 1, right_index + 1]


if __name__ == "__main__":
    print(Solution().twoSum(numbers=[2, 7, 11, 15], target=9))
    print(Solution().twoSum(numbers=[2, 3, 4], target=6))
    print(Solution().twoSum(numbers=[-1, 0], target=-1))
