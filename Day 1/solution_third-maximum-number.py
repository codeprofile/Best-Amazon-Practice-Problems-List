from typing import List


class Solution:
    """
    Problem statement : https://leetcode.com/problems/third-maximum-number/
    """

    def thirdMax(self, nums: List[int]) -> int:
        # getting unique values
        unique_nums = list(set(nums))
        # sorting the unique values in descending order with help of reverse keyword
        unique_nums.sort(reverse=True)
        try:
            # python index starts with 0 , 3rd max then will on index 2
            output = unique_nums[2]
        except Exception as e:
            # problem statement says if 3rd max is not present then return  maximum value present
            output = max(nums)
        return output


if __name__ == "__main__":
    print(Solution().thirdMax([3, 2, 1]))
    print(Solution().thirdMax([1, 2]))
    print(Solution().thirdMax([2, 2, 3, 1]))
