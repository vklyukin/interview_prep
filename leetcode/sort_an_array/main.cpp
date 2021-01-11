#include <random>;

class Solution {
 public:
  size_t MakePartition(std::vector<int>& nums, size_t start, size_t end,
                       size_t pivot_id) {
    int pivot = nums[pivot_id];

    int64_t left = start;
    int64_t right = end;

    while (left <= right) {
      while (nums[left] < pivot) {
        ++left;
      }

      while (nums[right] > pivot) {
        --right;
      }

      if (left < right) {
        std::swap(nums[left], nums[right]);
        ++left;
        --right;
      } else {
        return right;
      }
    }

    return right;
  }

  void QuickSort(std::vector<int>& nums, size_t start, size_t end,
                 std::mt19937& gen) {
    while (start < end) {
      std::uniform_int_distribution<size_t> dist(start, end);
      size_t pivot_id = dist(gen);

      pivot_id = MakePartition(nums, start, end, pivot_id);

      QuickSort(nums, start, pivot_id, gen);

      start = pivot_id + 1;
    }
  }

  vector<int> sortArray(vector<int>& nums) {
    std::mt19937 gen;
    QuickSort(nums, 0, nums.size() - 1, gen);
    return nums;
  }
};