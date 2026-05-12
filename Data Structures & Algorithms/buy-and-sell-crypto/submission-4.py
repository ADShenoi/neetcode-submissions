class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        total = 0
        lowest = prices[0]
        while i < len(prices):
            if prices[i] < lowest:
                lowest = prices[i]
            elif prices[i] > lowest:
                total = max(total,prices[i] - lowest)
            i += 1
        return total

