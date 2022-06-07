from typing import List


class Solution:
    """
    Problem statement : https://leetcode.com/problems/3sum/
    Solution understanding video link : https://www.youtube.com/watch?v=jzZsG8n2R9A
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        # sorting the array to avoid duplicate calculation
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1  # left pointer
            r = len(nums) - 1  # right pointer
            while l < r:
                summation = nums[i] + nums[l] + nums[r]
                # decreasing (as we are moving in the reverse direction) right pointer as it has greater value
                if summation > 0:
                    r -= 1
                # increment left pointer as the value in the left will be comparative less than right index pointer
                elif summation < 0:
                    l += 1
                else:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    # avoiding duplicate calculation and making sure left index does cross right pointer
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return output


if __name__ == "__main__":
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
