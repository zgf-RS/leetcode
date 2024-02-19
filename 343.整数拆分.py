#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0]*(60)
        dp[2] = 1
        # dp[3] = 2
        dp[3] = 2
        dp[4] = 4
        dp[5] =6
        dp[6] = 9
        i = 7
        while i <= n:
            dp[i] = max([3*dp[i-3],2*dp[i-2]])
            i += 1
        return dp[n]
# @lc code=end

