class Solution:
    def get_sum_of_cyphers(self, n: int) -> int:
        answer = 0
        while n > 9:
            n, last = divmod(n, 10)
            answer += last * last
        answer += n * n
        return answer

    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            else:
                seen.add(n)
                n = self.get_sum_of_cyphers(n)
        return True
