class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bp = prices[0]
        profit = 0
        i = 0
        while i < len(prices):
            if prices[i] < bp:
                bp = prices[i]
                
            profit = max(profit, prices[i] - bp)
            i += 1


        
        return profit