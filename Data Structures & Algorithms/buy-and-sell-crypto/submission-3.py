class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = 0
        # buy = prices[0]

        # for sell in prices:
        #     if sell - buy > profit:
        #         profit = sell - buy
        #     elif sell < buy:
        #         buy = sell

        # return profit

        max_profit = 0
        min_buy = prices[0]

        for sell in prices:
            max_profit = max(max_profit, sell - min_buy)
            min_buy = min(min_buy, sell)

        return max_profit