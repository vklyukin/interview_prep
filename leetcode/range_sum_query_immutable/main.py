# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


class NumArray:
    def __init__(self, nums: List[int]):
        self.cumsum = nums.copy()
        self.nums = nums

        for i in range(len(self.cumsum)):
            if i > 0:
                self.cumsum[i] += self.cumsum[i - 1]
            else:
                self.cumsum[i] = 0

    def sumRange(self, i: int, j: int) -> int:
        return self.cumsum[j] - self.cumsum[i] + self.nums[i]
