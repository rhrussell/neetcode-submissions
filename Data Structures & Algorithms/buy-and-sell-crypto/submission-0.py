class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
# profit = sell - buy or profit = prices[i] - buy
# [7, 1, 5, 3, 6, 4, 8, 5, 12, 1]
        for sell in prices:
            if sell - buy > profit:
                profit = sell - buy
            elif sell < buy:
                buy = sell

        return profit