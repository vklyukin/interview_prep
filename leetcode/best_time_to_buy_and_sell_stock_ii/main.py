class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        prev_val = -1
        for i, val in enumerate(prices):
            if i == 0:
                prev_val = val
                continue
            else:
                if val > prev_val:
                    profit += val - prev_val
                prev_val = val
        return profit
