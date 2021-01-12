#include <algorithm>
#include <unordered_map>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */

class Solution {
 public:
  int rob(TreeNode* root) {
    node_values.clear();

    if (!root) {
      return 0;
    }

    auto left_child_number = leftChildNumber(0);
    auto right_child_number = rightChildNumber(0);

    return std::max(robHelper(root->right, right_child_number, true) +
                        robHelper(root->left, left_child_number, true) +
                        root->val,
                    robHelper(root->right, right_child_number, false) +
                        robHelper(root->left, left_child_number, false));
  }

  inline uint64_t leftChildNumber(uint64_t parent_number) {
    return 2 * parent_number + 1;
  }

  inline uint64_t rightChildNumber(uint64_t parent_number) {
    return 2 * parent_number + 2;
  }

  int robHelper(TreeNode* child, uint64_t child_number, bool is_parent_robbed) {
    int child_case_factor = is_parent_robbed ? 1 : -1;
    uint64_t actual_child_number = child_case_factor * child_number;

    if (node_values.find(actual_child_number) != node_values.end()) {
      return node_values[actual_child_number];
    }

    if (!child) {
      node_values[actual_child_number] = 0;
      return 0;
    }

    auto left_child_number = leftChildNumber(child_number);
    auto right_child_number = rightChildNumber(child_number);

    if (!is_parent_robbed) {
      auto node_value = std::max(
          robHelper(child->right, right_child_number, true) +
              robHelper(child->left, left_child_number, true) + child->val,
          robHelper(child->right, right_child_number, false) +
              robHelper(child->left, left_child_number, false));
      node_values[actual_child_number] = node_value;
      return node_value;
    }

    auto node_value = robHelper(child->right, right_child_number, false) +
                      robHelper(child->left, left_child_number, false);
    node_values[actual_child_number] = node_value;
    return node_value;
  }

 private:
  unordered_map<uint64_t, int> node_values;
};