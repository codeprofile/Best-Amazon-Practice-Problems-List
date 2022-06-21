# Learning
"""
>> Inversion : Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j
"""


class Solution:
    """
    Problem Statement : https://www.geeksforgeeks.org/counting-inversions/
    We Will be Solving this problem using `Enhanced Merge sort `
    Enhanced Merge sort Algorithm:
    >> The idea is similar to merge sort, divide the array into two equal or almost equal halves in each step until the base case is reached.
    >> Create a function merge that counts the number of inversions when two halves of the array are merged,
        create two indices i and j, i is the index for the first half, and j is an index of the second half.
        if a[i] is greater than a[j], then there are (mid – i) inversions. because left and right subarrays are sorted,
        so all the remaining elements in left-subarray (a[i+1], a[i+2] … a[mid]) will be greater than a[j].
    >> Create a recursive function to divide the array into halves and find the answer by summing the number of inversions is the first half,
        the number of inversion in the second half and the number of inversions by merging the two.
    >> The base case of recursion is when there is only one element in the given half.
    >> Print the answer

    Time Complexity: O(n log n), The algorithm used is divide and conquer,
    So in each level, one full array traversal is needed, and there are log n levels, so the time complexity is O(n log n).
    Space Complexity: O(n), Temporary array.
    """

    def merge(self, arr, temp_arr, left, mid, right):
        i = left  # Starting index of left subarray
        j = mid + 1  # Starting index of right subarray
        k = left  # Starting index of to be sorted subarray
        inv_count = 0
        # Conditions are checked to make sure that i and j don't exceed their subarray limits.
        while i <= mid and j <= right:
            # There will be no inversion if arr[i] <= arr[j]
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                k += 1
                i += 1
            else:
                # Inversion will occur
                temp_arr[k] = arr[j]
                inv_count += (mid - i + 1)
                k += 1
                j += 1
        # Copy the remaining elements of left subarray into temporary array
        while i <= mid:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        # Copy the remaining elements of right subarray into temporary array
        while j <= right:
            temp_arr[k] = arr[j]
            k += 1
            j += 1

        # Copy the sorted subarray into Original array
        for loop_var in range(left, right + 1):
            arr[loop_var] = temp_arr[loop_var]

        return inv_count

    def _mergeSort(self, arr, temp_arr, left, right):
        # A variable inv_count is used to store inversion counts in each recursive call
        inv_count = 0
        # we will make a recursive call if and only if we have more than one elements

        if left < right:
            # mid is calculated to divide the array into two subaaray
            # Floor division is must in case of python
            mid = (left + right) // 2
            # It will calculate inversion counts in the left subarray
            inv_count += self._mergeSort(arr, temp_arr, left, mid)

            # It will calculate inversion counts in right subarray
            inv_count += self._mergeSort(arr, temp_arr, mid + 1, right)
            # It will merge 2 subarray in a sorted array
            inv_count += self.merge(arr, temp_arr, left, mid, right)
        return inv_count

    def mergeSort(self, arr):
        # A temp_arr is created to store sorted array in merge function
        temp_arr = [0] * len(arr)
        return self._mergeSort(arr, temp_arr, 0, len(arr) - 1)


if __name__ == "__main__":
    arr = [1, 20, 6, 4, 5]
    result = Solution().mergeSort(arr)
    print("Number of inversions are", result)
