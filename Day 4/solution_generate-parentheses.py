from typing import List


class Solution:
    """
    Problem statement : https://leetcode.com/problems/generate-parentheses/
    using recursion
    """

    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def rec(left_p, right_p, stack, cand):

            if left_p == right_p == 0:
                output.append(cand)
                return
            if left_p > 0:
                rec(left_p - 1, right_p, stack + 1, cand + "(")

            if right_p > 0 and stack > 0:
                rec(left_p, right_p - 1, stack - 1, cand + ")")

        rec(n, n, 0, "")
        return output


if __name__ == "__main__":
    print(Solution().generateParenthesis(n=3))
    print(Solution().generateParenthesis(n=1))
