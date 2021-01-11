#include <algorithm>;

class Solution {
 public:
  void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
    vector<int> nums_buffer;

    size_t second_index = 0;
    size_t buffer_index = 0;

    for (size_t first_index = 0; first_index < nums1.size(); ++first_index) {
      if (second_index >= nums2.size() && buffer_index >= nums_buffer.size()) {
        return;
      }

      if (nums1[first_index] == 0 &&
          first_index >= m) {  // There is no element in 1st array

        if (buffer_index < nums_buffer.size() && second_index < nums2.size()) {
          if (nums2[second_index] < nums_buffer[buffer_index]) {
            nums1[first_index] = nums2[second_index];
            ++second_index;
          } else {
            nums1[first_index] = nums_buffer[buffer_index];
            ++buffer_index;
          }

        } else if (buffer_index < nums_buffer.size()) {
          nums1[first_index] = nums_buffer[buffer_index];
          ++buffer_index;
        } else if (second_index < nums2.size()) {
          nums1[first_index] = nums2[second_index];
          ++second_index;
        }

      } else if (second_index < nums2.size() &&
                 nums1[first_index] > nums2[second_index] &&
                 (buffer_index >= nums_buffer.size() ||
                  nums_buffer[buffer_index] > nums2[second_index])) {
        // There is an element in 1st array and
        // it's greater than current element in 2nd array
        // and current element in buffer
        nums_buffer.push_back(nums1[first_index]);
        nums1[first_index] = nums2[second_index];
        ++second_index;
      } else if (buffer_index < nums_buffer.size()) {
        // The buffer is not empty
        nums_buffer.push_back(nums1[first_index]);
        nums1[first_index] = nums_buffer[buffer_index];
        ++buffer_index;
      }
    }
  }
};
