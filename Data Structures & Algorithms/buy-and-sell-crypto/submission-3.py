class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        stat = 0 
        end = 1 
        profit = 0 

        while end < len(prices):
            if prices[stat] < prices[end]:
                val = prices[end] - prices[stat]
                profit = max(profit, val)
            else:
                stat = end
            end += 1

        return profit