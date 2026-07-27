class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # we simply sum all possible profits, when there is a value
        # that is greater than the prev day we calc the profit and add it to the total


        profit = 0

        for i in range(0, len(prices) - 1):
            if prices[i] < prices[i+1]:
                profit += prices[i+1] - prices[i]

        return profit
        