class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return []
        left_product = [1]
        for num in nums:
            left_product.append(left_product[-1] * num)
        left_product.pop()

        right_product = [1]
        for num in reversed(nums):
            right_product.append(right_product[-1] * num)
        right_product.pop()
        right_product.reverse()

        return [left_product[i] * right_product[i] for i in range(len(nums))]
