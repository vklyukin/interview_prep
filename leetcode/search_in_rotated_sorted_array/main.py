class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left_id, right_id = 0, len(nums)
        while left_id + 1 < right_id:
            mid_id = left_id + (right_id - left_id) // 2
            # left half: [left_id, mid_id)
            # right_half: [mid_id, right_id)

            if nums[left_id] <= nums[mid_id - 1]:
                if nums[left_id] <= target <= nums[mid_id - 1]:
                    right_id = mid_id
                else:
                    left_id = mid_id
            else:
                if nums[mid_id] <= target <= nums[right_id - 1]:
                    left_id = mid_id
                else:
                    right_id = mid_id

        if nums[left_id] == target:
            return left_id
        else:
            return -1
