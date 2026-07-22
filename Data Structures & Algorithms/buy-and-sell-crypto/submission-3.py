class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l, r = 0, 1
        max_profit = 0
        # [7,1,5,3,6,4]
        while l < len(prices) and r < len(prices):
            
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
                r += 1 
            
            elif prices[r] <= prices[l]:
                l = r
                r = l + 1

        return max_profit
