class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = set(nums1)
        nums3 = []

        for num in nums2:

            if num in counter:
                counter.remove(num)
                nums3.append(num)

        return nums3