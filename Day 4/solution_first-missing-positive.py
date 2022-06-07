from typing import List


class Solution:
    """
    Problem statement : https://leetcode.com/problems/first-missing-positive/
    https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array/
    Approach used here :
    >> The smallest positive integer is 1. First we will check if 1 is present in the array or not.
        If it is not present then 1 is the answer.
    >> If present then, again traverse the array. The largest possible answer is N+1 where N is the size of array.
        This will happen when array have all the elements from 1 to N. When we are traversing the array,
        if we find any number less than 1 or greater than N, then we will change it to 1.
        This will not change anything as answer will always between 1 to N+1. Now our array has elements from 1 to N.
    >> Now, for every ith number, increase arr[ (arr[i]-1) ] by N.
        But this will increase the value more than N. So, we will access the array by arr[(arr[i]-1)%N].
        What we have done is for each value we have increased value at that index by N.
    >> We will find now which index has value less than N+1. Then i+1 will be our answer.
    """

    def firstMissingPositive(self, nums: List[int]) -> int:
        ptr = 0
        n = len(nums)
        # Check if 1 is present in array or not
        for i in range(n):
            if nums[i] == 1:
                ptr = 1
                break

        # If 1 is not present
        if ptr == 0:
            return 1

        # Changing values to 1
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        # Updating indices according to values
        for i in range(n):
            nums[(nums[i] - 1) % n] += n

        # Finding which index has value less than n
        for i in range(n):
            if nums[i] <= n:
                return i + 1
        # If array has values from 1 to n
        return n + 1


if __name__ == "__main__":
    print(Solution().firstMissingPositive([1, 2, 0]))
    print(Solution().firstMissingPositive([3, 4, -1, 1]))
    print(Solution().firstMissingPositive([7, 8, 9, 11, 12]))
