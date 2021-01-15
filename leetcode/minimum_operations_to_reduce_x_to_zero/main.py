class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target_sum = sum(nums) - x
        len_nums = len(nums)

        if target_sum < 0:
            return -1
        elif target_sum == 0:
            return len_nums

        current_sum = 0
        max_length = 0
        left = 0

        for right in range(len_nums):

            current_sum += nums[right]

            while current_sum >= target_sum:

                if current_sum == target_sum:
                    max_length = max(max_length, right - left + 1)

                current_sum -= nums[left]
                left += 1

        if max_length == 0:
            return -1

        return len_nums - max_length
