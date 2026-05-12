class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bp = prices[0]
        profit = 0

        for p in prices:
            if p < bp:
                bp = p
            
            profit = max(profit, p-bp)
        
        return profit