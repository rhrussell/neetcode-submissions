class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_num = prices[0]

        for price in prices:
            if price < min_num:
                min_num = price
            if price - min_num > profit:
                profit = price - min_num

        return profit