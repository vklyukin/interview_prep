/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
struct LeveledNode {
    TreeNode* node = nullptr;
    int level = 0;
};

class Solution {
public:
    vector<int> largestValues(TreeNode* root) {
        std::vector<int> largest_values;
        
        LeveledNode root_node{root, 0};
        std::deque<LeveledNode> queue{root_node};
        
        while (!queue.empty()) {
            
            auto node = queue.front();
            queue.pop_front();
            
            if (!node.node) {
                continue;
            }
            
            if (largest_values.size() == node.level) {
                largest_values.push_back(node.node->val);
            } else if (largest_values[node.level] < node.node->val) {
                largest_values[node.level] = node.node->val;
            }
            
            LeveledNode left_child{node.node->left, node.level + 1};
            LeveledNode right_child{node.node->right, node.level + 1};
            
            queue.push_back(left_child);
            queue.push_back(right_child);
        }
        
        return largest_values;
    }
};