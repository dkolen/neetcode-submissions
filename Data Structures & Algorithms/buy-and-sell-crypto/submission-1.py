class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minL = prices[0]
        profit = 0
        for i in range(len(prices)):
            profit = max(profit, prices[i] - minL)
            minL = min(minL, prices[i])
        return profit
