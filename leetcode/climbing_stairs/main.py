class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1

        prev1, prev2 = 1, 1

        for step in range(2, n):
            prev1, prev2 = prev2, prev1
            prev1 = prev2 + prev1

        return prev2 + prev1
