# max_rob(i) = max(max_rob(i + 2) + nums[i], max_rob(i + 1))
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_max_rob, prev_prev_max_rob = 0, 0
        max_rob = 0
        for num in nums:
            cur_max_rob = max(prev_max_rob, prev_prev_max_rob + num)
            max_rob = max(max_rob, cur_max_rob)
            prev_prev_max_rob, prev_max_rob = prev_max_rob, cur_max_rob

        return max_rob
