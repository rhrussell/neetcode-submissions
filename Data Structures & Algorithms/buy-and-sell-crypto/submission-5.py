class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_buy = prices[0]

        for price in prices:
            profit = max(profit, price - min_buy)
            min_buy = min(min_buy, price)

        return profit