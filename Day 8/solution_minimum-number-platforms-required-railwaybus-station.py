# Learning
"""
>> Python uses Timsort in its sort() method.

>> It is a hybrid sorting algorithm that uses both merge sort and insertion sorting techniques.

>> Worst-case performance O(nlogn)

>> Best-case performance O(n)

>> Average performance O(nlogn)

>> Worst-case space complexity O(n)
"""


class Solution:
    """
    Problem Statement : https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/
    Algorithm:
    >> Sort the arrival and departure times of trains.
    >> Create 2 pointers i=1 & j=0 ,and a variable to store result and current count platform
    >> Run a loop while i <n and j< n and compare the ith element of arrival array and jth element of departure array
    >> If the arrival time is less than or equal to departure then one more platform is needed so increase the count i.e.,
    platform ++ and increment i
    >>Else if the arrival time is greater than departure then one less platform is needed to decrease the count , ie. platform -- and
    increment j
    >> Update the ans , i.e result = max(result,platform)
    Implementation:
    This doesn't create a single sorted list of all events, rather it individually
    sorts arr[] and dep[] arrays, and then uses the merge process of merge sort to process them
    together as a single sorted array
    Time Complexity: O(N * log N), One traversal O(n) of both the array is needed after sorting O(N * log N).
    Auxiliary space: O(1), As no extra space is required.
    """

    def findPlatform(self, arrival: list, departure: list)->int:
        arrival.sort()
        departure.sort()

        platform = 1
        result = 1
        i = 1
        j = 0

        while i < len(arrival) and j < len(departure):
            if arrival[i] <= departure[j]:
                platform += 1
                i += 1
            elif arrival[i] > departure[j]:
                platform -= 1
                j += 1
            if platform > result:
                result = platform
        return result


if __name__ == "__main__":
    arr = [900, 940, 950, 1100, 1500, 1800]
    dep = [910, 1200, 1120, 1130, 1900, 2000]

    print("Minimum Number of Platforms Required = ",
          Solution().findPlatform(arr, dep))
