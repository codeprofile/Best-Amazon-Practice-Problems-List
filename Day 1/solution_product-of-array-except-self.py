from typing import List


class MyFailedAttempt:
    """
    below function was my 1st attempt to solve problem .
    It Failed on leetcode because of Time Exceed issue .
    though it has o(1) space complexity . but time complexity as o(n^2)
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initializing output list
        output = []
        # Iterating through array taking each indices
        for i in range(len(nums)):
            # Initializing multiplier
            multiplier = 1
            # Again Iterating through array for getting values
            for j, element in enumerate(nums):
                if i == j:
                    # ignoring the current self index
                    pass
                else:
                    # getting product of elements
                    multiplier = multiplier * element
            output.append(multiplier)
        return output


class Solution:
    """
       Problem statement : https://leetcode.com/problems/product-of-array-except-self/
       Solution understanding video link : https://www.youtube.com/watch?v=bNvIQI2wAjk
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initializing output array with value 1 and as same size of input array
        res = [1] * len(nums)
        # Input array till the current ignoring index is considered as prefix array and
        # prefix value is product all the prefix value present in the prefix array .
        # Here we do not allocate an auxiliary space for Prefix array it's directly stored in the res array
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]  # product of prefix value for instance : res[0] will get 1 (prefix default value)
            # then num[0] will be multiplied to prefix .It multiplication goes till the array does not get exhausted.
        suffix = 1
        # suffix will traverse the array in the reverse order and
        # use the same value present in res array using prefix value
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res


if __name__ == "__main__":
    print(MyFailedAttempt().productExceptSelf([1, 2, 3, 4]))
    print(MyFailedAttempt().productExceptSelf([-1, 1, 0, -3, 3]))
    print(Solution().productExceptSelf([1, 2, 3, 4]))
    print(Solution().productExceptSelf([-1, 1, 0, -3, 3]))
