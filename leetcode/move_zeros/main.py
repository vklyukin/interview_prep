class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        zero_ptr, nnz_ptr = 0, len_nums - 1

        while nnz_ptr < len_nums:
            while zero_ptr < len_nums and nums[zero_ptr] != 0:
                zero_ptr += 1

            nnz_ptr = zero_ptr
            while nnz_ptr < len_nums and nums[nnz_ptr] == 0:
                nnz_ptr += 1

            if nnz_ptr < len_nums:
                nums[zero_ptr], nums[nnz_ptr] = nums[nnz_ptr], nums[zero_ptr]
                zero_ptr += 1
                nnz_ptr += 1
