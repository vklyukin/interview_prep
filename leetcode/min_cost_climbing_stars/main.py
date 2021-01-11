class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_costs = [0] * (len(cost) + 1)

        for step in range(2, len(min_costs)):
            min_costs[step] = min(
                min_costs[step - 1] + cost[step - 1],
                min_costs[step - 2] + cost[step - 2],
            )

        return min_costs[-1]