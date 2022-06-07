from typing import List


class Solution:
    """
    Problem statement : https://leetcode.com/problems/get-the-maximum-score/
    Using 2 pointer technique
    https://www.tutorialspoint.com/program-to-find-the-maximum-score-from-all-possible-valid-paths-in-python
    """

    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        sum1 = 0
        sum2 = 0
        i = 0
        j = 0

        # traversing both the array simultaneously
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                # value of num1 is less than num2 than sum1  holds the value of nums1
                sum1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:  # if num1 is greater than sum2 holds the value of nums2
                sum2 += nums2[j]
                j += 1
            else:
                ans += max(sum1, sum2) + nums1[i]
                sum1 = 0
                sum2 = 0
                i += 1
                j += 1
        while i < len(nums1):
            sum1 += nums1[i]
            i += 1

        while j < len(nums2):
            sum2 += nums2[j]
            j += 1

        return (ans + max(sum1, sum2)) % (10 ** 9 + 7)


if __name__ == "__main__":
    print(Solution().maxSum(nums1=[2, 4, 5, 8, 10],nums2=[4, 6, 8, 9]))