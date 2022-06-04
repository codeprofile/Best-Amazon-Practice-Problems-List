class Solution:
    """
    Problem statement : https://leetcode.com/problems/longest-substring-without-repeating-characters/
    Solution understanding video link :https://www.youtube.com/watch?v=wiGpQwVHdE0
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initializing character set to hold unique character
        charset = set()
        # left index will be a index for charset
        left_index = 0
        res = 0
        for right_index in range(len(s)):
            # Removing character if present in charset
            while s[right_index] in charset:
                charset.remove(s[left_index])
                left_index += 1
            # Adding character in the charset
            charset.add(s[right_index])
            res = max(res, (right_index - left_index + 1))
        return res


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
    print(Solution().lengthOfLongestSubstring("bbbb"))
    print(Solution().lengthOfLongestSubstring("pwwkew"))
