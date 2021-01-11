class Solution {
 public:
  bool canJump(vector<int>& nums) {
    if (nums.size() <= 1) {
      return true;
    }

    size_t size = nums.size();
    int left_most = size - 1;

    for (int i = size - 2; i >= 0; --i) {
      if (i + nums[i] >= left_most) {
        left_most = i;
      }
    }

    return left_most == 0;
  }
};
