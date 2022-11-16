"""
22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        """
        2022-11-14
        Approach: dynamic programming
        1) define subproblem: denote p[i] as all combinations of well-formed parentheses with i pairs
        2) recurrence: p[i] = union("(" + p[i-j-1] + ")" + p[j], p[j] + "(" + p[i-j-1] + ")"), for j = 0..i-1,
                        and duplicates should be counted as 1
        3) base cases: p[0] = [""]

        Time complexity :
        """
        dp = {0: [""]}
        for i in range(1, n+1):
            p = []
            for j in range(0, i):
                p += ["("+x+")" + y for x in dp[i-j-1] for y in dp[j]]
                p += [x + "("+y+")" for x in dp[i-j-1] for y in dp[j]]
            dp[i] = list(set(p))
        return dp[n]