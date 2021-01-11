from random import randint


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(nums: List[int], first: int, last: int):
            if last - first < 1:
                return nums

            l, r = first, last

            pivot = nums[randint(l, r)]

            while l <= r:

                while nums[l] < pivot:
                    l += 1

                while nums[r] > pivot:
                    r -= 1

                if l <= r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1

            quicksort(nums, first, r)
            quicksort(nums, l, last)

            return nums

        return quicksort(nums, 0, len(nums) - 1)