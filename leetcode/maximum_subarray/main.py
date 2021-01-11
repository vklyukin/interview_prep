# max_sum(i) = max(max_sum(i - 1) + nums[i], nums[i])


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev_max_sum = 0
        max_sum = float("-inf")

        for num in nums:
            cur_max_sum = max(prev_max_sum + num, num)
            max_sum = max(cur_max_sum, max_sum)
            prev_max_sum = cur_max_sum

        return max_sum
