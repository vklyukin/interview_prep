
// Definition for singly-linked list.
struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
 public:
  ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
    bool to_inc = false;
    ListNode *answer = nullptr;
    ListNode *prev_digit = nullptr;

    while (l1 && l2) {
      int new_val = l1->val + l2->val + (to_inc ? 1 : 0);
      if (new_val > 9) {
        new_val %= 10;
        to_inc = true;
      } else {
        to_inc = false;
      }

      ListNode *cur_digit = new ListNode(new_val);
      if (!prev_digit) {
        prev_digit = cur_digit;
        answer = prev_digit;
      } else {
        prev_digit->next = cur_digit;
        prev_digit = cur_digit;
      }

      l1 = l1->next;
      l2 = l2->next;
    }

    while (l1) {
      int new_val = l1->val + (to_inc ? 1 : 0);
      if (new_val > 9) {
        new_val %= 10;
        to_inc = true;
      } else {
        to_inc = false;
      }

      ListNode *cur_digit = new ListNode(new_val);
      if (!prev_digit) {
        prev_digit = cur_digit;
        answer = prev_digit;
      } else {
        prev_digit->next = cur_digit;
        prev_digit = cur_digit;
      }

      l1 = l1->next;
    }

    while (l2) {
      int new_val = l2->val + (to_inc ? 1 : 0);
      if (new_val > 9) {
        new_val %= 10;
        to_inc = true;
      } else {
        to_inc = false;
      }

      ListNode *cur_digit = new ListNode(new_val);
      if (!prev_digit) {
        prev_digit = cur_digit;
        answer = prev_digit;
      } else {
        prev_digit->next = cur_digit;
        prev_digit = cur_digit;
      }

      l2 = l2->next;
    }

    if (to_inc) {
      ListNode *cur_digit = new ListNode(1);
      if (!prev_digit) {
        prev_digit = cur_digit;
        answer = prev_digit;
      } else {
        prev_digit->next = cur_digit;
        prev_digit = cur_digit;
      }
    }

    return answer;
  }
};
