class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_length = 0
        cur_count = 0
        counts = {cur_count: -1}

        for i, num in enumerate(nums):
            cur_count += num * 2 - 1
            if cur_count in counts:
                max_length = max(max_length, i - counts[cur_count])
            else:
                counts[cur_count] = i

        return max_length
