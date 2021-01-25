class Solution {
 public:
  bool kLengthApart(vector<int>& nums, int k) {
    int last_seen_one_index = -1;

    for (auto index = 0; index < nums.size(); ++index) {
      if (nums[index] == 1) {
        if (last_seen_one_index != -1 && index - last_seen_one_index <= k) {
          return false;
        }

        last_seen_one_index = index;
      }
    }

    return true;
  }
};