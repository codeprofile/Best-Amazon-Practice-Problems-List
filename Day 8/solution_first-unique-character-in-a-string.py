import collections


class Solution:
    """
    problem statement :https://leetcode.com/problems/first-unique-character-in-a-string/
    self-written solution with linear time complexity O(n)
    """

    def firstUniqChar(self, s: str) -> int:
        count_map = collections.Counter(s)
        for index, char in enumerate(s):
            if count_map[char] == 1:
                return index
            else:
                continue
        else:
            return -1


if __name__ == "__main__":
    print(Solution().firstUniqChar("leetcode"))
