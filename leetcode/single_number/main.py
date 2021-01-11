class Solution:
    def singleNumber(self, nums):
        answer = 0

        for i in nums:
            answer ^= i

        return answer