class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bp = prices[0]
        profit = 0
        i = 0
        while i < len(prices):
            print(prices[i], bp)
            if prices[i] > bp:
                profit = max(profit, prices[i] - bp)
            if prices[i] < bp:
                bp = prices[i]
            i += 1
        
        return profit