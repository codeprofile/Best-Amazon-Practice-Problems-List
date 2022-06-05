from typing import List


class Solution:
    """
    Problem statement : https://leetcode.com/problems/container-with-most-water/
    Solution understanding video link :https://www.youtube.com/watch?v=UuiTKBwPgAo
    Using 2 pointer technique
    """

    def maxArea(self, height: List[int]) -> int:
        res = 0
        # setting left point to index 0 and right pointer to last element index
        left_pt, right_pt = 0, len(height) - 1
        while left_pt < right_pt:
            # right_index - left_index will give you distance of vertical line or length
            # min(height[right_pt], height[left_pt]) will provide you with the height or width/breadth
            area = (right_pt - left_pt) * min(height[right_pt], height[left_pt])
            # getting the maximum area value .
            res = max(res, area)
            # Moving ahead if left_pointer height is lower than right and vice verse for right_pointer
            if height[left_pt] < height[right_pt]:
                left_pt += 1
            else:
                right_pt -= 1
        return res


if __name__ == "__main__":
    print(Solution().maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(Solution().maxArea(height=[1, 1]))
