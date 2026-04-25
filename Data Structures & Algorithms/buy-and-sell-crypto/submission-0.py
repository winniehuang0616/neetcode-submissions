class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            buy = prices[i]
            sell = 0
            for k in range(i+1, len(prices)):
                sell = max(sell, prices[k]-buy)
            res = max(res, sell)
        return res
        