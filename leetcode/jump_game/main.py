# can_jump(i) = can_jump(i + 1) | ... | can_jump(i + nums[i])
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nums_len = len(nums)
        left_most = nums_len - 1

        for i in range(nums_len - 2, -1, -1):
            if i + nums[i] >= left_most:
                left_most = i

        return left_most == 0
