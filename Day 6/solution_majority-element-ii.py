from typing import List
import collections


class Solution:
    """
    problem statement : https://leetcode.com/problems/majority-element-ii/
    """

    def majorityElement(self, nums: List[int]) -> List[int]:
        length = len(nums)
        # collection.Counter takes list and converts into dictionary of integer and it's count
        counter = collections.Counter(nums)

        if length < 3:
            return list(counter.keys())

        result = []

        words = counter.most_common(3)
        for i in range(0, min(3, len(counter))):
            if words[i][-1] > length / 3:
                result.append(words[i][0])
        return result


if __name__ == "__main__":
    print(Solution().majorityElement(nums=[3, 2, 3]))
