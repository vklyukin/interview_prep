/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
 public:
  ListNode* mergeKLists(vector<ListNode*>& lists) {
    size_t k = lists.size();

    std::priority_queue<pair<int, int>, std::vector<pair<int, int>>,
                        std::greater<pair<int, int>>>
        heap;
    ListNode* output_head = nullptr;
    ListNode* output_tail = nullptr;

    for (auto list_index = 0; list_index < k; ++list_index) {
      if (!lists[list_index]) {
        continue;
      }

      heap.push(std::make_pair(lists[list_index]->val, list_index));
      lists[list_index] = lists[list_index]->next;
    }

    while (!heap.empty()) {
      auto value_index = heap.top();
      auto value = value_index.first;
      auto index = value_index.second;
      heap.pop();

      auto new_node = new ListNode(value);
      if (!output_head) {
        output_head = output_tail = new_node;
      } else {
        output_tail->next = new_node;
        output_tail = output_tail->next;
      }

      if (lists[index]) {
        heap.push(std::make_pair(lists[index]->val, index));
        lists[index] = lists[index]->next;
      }
    }

    return output_head;
  }
};