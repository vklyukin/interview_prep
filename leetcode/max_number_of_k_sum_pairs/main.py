# [1]; 1
# [1]; 2
# [1,2]; 3
# [1, 2, 2]; 3
# [1, 1, 2, 2]; 3


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        left_index = 0
        right_index = len(nums) - 1

        max_operations = 0

        while left_index < right_index:
            left_right_sum = nums[left_index] + nums[right_index]

            if left_right_sum < k:
                left_index += 1
            elif left_right_sum > k:
                right_index -= 1
            else:
                max_operations += 1
                left_index += 1
                right_index -= 1

        return max_operations
