class Solution:
    def numTrees(self, n: int) -> int:

        # n = 3
        # dp(3) = dp(0) * dp(2) + dp(1) * dp(1) + dp(2) * dp(1)

        dp = [1] * (n+1)
        for i in range(2, n+1):
            total = 0
            for j in range(1, i+1):
                left = j - 1
                right = i - j
                total += dp[left] * dp[right]
            dp[i] = total
        return dp[n]