from typing import List


class Solution:
    """
    Problem statement : https://leetcode.com/problems/trapping-rain-water/
    Solution understanding video link :https://www.youtube.com/watch?v=ZI2z5pq0TqA
    Using 2 pointer technique
    """

    def trap(self, height: List[int]) -> int:
        if not height: return 0
        # Initialing 2 pointers
        left_pt, right_pt = 0, len(height) - 1
        # tracking max height of left index and right index
        leftMax, rightMax = height[left_pt], height[right_pt]
        res = 0
        while left_pt < right_pt:
            if leftMax < rightMax:
                # Moving ahead if left height is less than right height
                left_pt += 1
                leftMax = max(leftMax, height[left_pt])
                res += leftMax - height[left_pt]  # amount of water that will get trapped
            else:
                # Moving ahead reverse direction i.e increasing right pointer
                right_pt -= 1
                rightMax = max(rightMax, height[right_pt])
                res += rightMax - height[right_pt]  # amount of water that will get trapped
        return res


if __name__ == "__main__":
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(Solution().trap([4, 2, 0, 3, 2, 5]))
