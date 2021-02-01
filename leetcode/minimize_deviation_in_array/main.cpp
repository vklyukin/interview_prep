class Solution {
 public:
  bool isEven(int number) { return number % 2 == 0; }

  bool isOdd(int number) { return !isEven(number); }

  int minimumDeviation(vector<int>& nums) {
    for (auto index = 0; index < nums.size(); ++index) {
      if (isOdd(nums[index])) {
        nums[index] = 2 * nums[index];
      }
    }

    std::set<int> tree_set(nums.begin(), nums.end());

    auto min_element_iter = tree_set.begin();
    auto max_element_iter = std::prev(tree_set.end());

    auto min_deviation = *max_element_iter - *min_element_iter;

    while (isEven(*max_element_iter)) {
      auto current_deviation = *max_element_iter - *min_element_iter;

      if (current_deviation < min_deviation) {
        min_deviation = current_deviation;
      }

      auto new_element = *max_element_iter / 2;

      tree_set.erase(max_element_iter);
      tree_set.insert(new_element);

      min_element_iter = tree_set.begin();
      max_element_iter = std::prev(tree_set.end());
    }

    auto current_deviation = *max_element_iter - *min_element_iter;

    if (current_deviation < min_deviation) {
      min_deviation = current_deviation;
    }

    return min_deviation;
  }
};