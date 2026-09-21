class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for sell_price in prices:
            if sell_price >= min_price:
                max_profit = max(max_profit, sell_price-min_price)
            else:
                min_price = sell_price
        
        return max_profit



# prices = [10,1,5,6,7,1]
# min_price = 10
# max_profit = 0

# The naive approach: n^2 solution where for each day we try to find the max difference it can achieve and do that for all days and keep a global max_profit tracker across all runs

# I think we just need to maximise the positive difference