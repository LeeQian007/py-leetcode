class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}  # key=(i, buying) val=max_profit

        def dfs(i, canWeBuying):
            if i >= len(prices):
                return 0
            if (i, canWeBuying) in dp:
                return dp[(i, canWeBuying)]

            # when you do a cooldown the flag of "canWeBuying" won't change
            cooldown = dfs(i + 1, canWeBuying)

            if canWeBuying:
                profitAfterBuy = dfs(i + 1, not canWeBuying) - prices[i]
                dp[(i, canWeBuying)] = max(profitAfterBuy, cooldown)
            else:
                profitAfterSell = dfs(i + 2, not canWeBuying) + prices[i]
                dp[(i, canWeBuying)] = max(profitAfterSell, cooldown)

            return dp[(i, canWeBuying)]

        return dfs(0, True)