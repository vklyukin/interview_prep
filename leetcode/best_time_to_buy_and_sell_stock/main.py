# profit(i, j) - max profit in [i, j]
# maxProfit = profit(0, n)
# profit()


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        prev_profit = 0
        for i, val in enumerate(prices):
            if i == 0:
                continue

            prev_profit += val - prices[i - 1]
            prev_profit = max(0, prev_profit)

            max_profit = max(prev_profit, max_profit)

        return max_profit