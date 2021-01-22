class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []

        for index, number in enumerate(nums):

            while (
                len(stack) != 0
                and stack[-1] > number
                and k - len(stack) <= len(nums) - index - 1
            ):
                stack.pop()

            if len(stack) < k:
                stack.append(number)

        return stack
