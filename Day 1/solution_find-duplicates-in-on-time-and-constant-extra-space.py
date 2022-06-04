class MyFailedAttempt:
    """
    below function was my 1st attempt to solve problem .
    It Failed on geeksforgeeks because of Time issue .
    It run successfully for 207/350 testcases.
    space complexity is not taken care of .
    """

    def duplicates(self, arr, n):
        # Initializing output list
        output = []
        # Iterating through array by taking index and element
        for index, element in enumerate(arr):
            # elements before index are considered in prefix_arr
            prefix_arr = arr[0:index]
            # elements after index are considered in prefix_arr
            postfix_arr = arr[index + 1:]
            # checking if the element is present in any of the list
            if element in set(prefix_arr) or element in set(postfix_arr):
                # if element is present it's appended to the final output list
                output.append(element)
        if len(output) == 0:
            # if no element are present -1 is appended in the list
            output.append(-1)
        # unique output elements in the sorted manner is returned in the output list
        output = list(set(output))
        output.sort()
        return output


class Solution:
    """
     Problem statement : https://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/
     Hints to solve the problem statement :
        >> 1- Traverse the given array from i= 0 to n-1 elements .
        Go to index arr[i]%n and increment its value by n.
        >> 2- Now traverse the array again and print all those
        indexes i for which arr[i]/n is greater than 1.

        This approach works because all elements are in range
        from 0 to n-1 and arr[i]/n would be greater than 1
        only if a value "i" has appeared more than once.
    """

    def duplicates(self, arr, n):
        # Initializing output list
        output = []
        # Traverse the given array from i= 0 to n-1 elements
        for i in range(0, n):
            # Go to index arr[i]%n and increment its value by n
            index = arr[i] % n
            arr[index] += n
        # Now traverse the array
        for i in range(0, n):
            # append  all those indexes i for which arr[i]/n is greater than 2
            if (arr[i] / n) >= 2:
                output.append(i)
        if len(output) == 0:
            output.append(-1)
        return output


if __name__ == '__main__':
    print(MyFailedAttempt().duplicates([0, 3, 1, 2], 4))
    print(Solution().duplicates([0, 3, 1, 2], 4))
