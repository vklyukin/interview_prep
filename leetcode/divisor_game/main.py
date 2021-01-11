# alice_wins(x) = any(alice_wins(k) for k in range(1, x + 1) if x % k == 0)


class Solution:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0