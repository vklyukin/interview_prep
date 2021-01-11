class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if n < 0:
            x = 1 / x if x != 0 else 0
            n = -n
        while n > 0:
            if n & 1:
                n -= 1
                res *= x
            else:
                n >>= 1
                x *= x
        return res
