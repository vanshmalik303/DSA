class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mini = prices[0]
        profit = 0

        for i in range(len(prices)):
            curr = prices[i] - mini

            profit = max(profit, curr)

            mini = min(mini, prices[i])

        return profit