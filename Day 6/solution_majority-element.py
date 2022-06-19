from typing import List


class Solution:
    """
    problem statement : https://leetcode.com/problems/majority-element/
    self-written solution with linear time complexity O(n)
    """

    def majorityElement(self, nums: List[int]) -> int:
        # creating a dictionary with all unique elements as key and initializing it's value to 0
        temp_dict = dict.fromkeys(set(nums), 0)
        for i in nums:
            # Increment the value count with 1 if key is repeated
            temp_dict[i] = temp_dict[i] + 1
        # returning the maximum value key from dictionary
        return max(temp_dict, key=lambda x: temp_dict[x])


if __name__ == "__main__":
    print(Solution().majorityElement(nums=[3, 2, 3]))
