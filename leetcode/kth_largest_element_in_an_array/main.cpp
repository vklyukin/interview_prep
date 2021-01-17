class Solution {
 public:
  int findKthLargest(vector<int>& nums, int k) {
    priority_queue<int, vector<int>, std::greater<int>> heap;

    for (auto element : nums) {
      heap.push(element);

      if (heap.size() == k + 1) {
        heap.pop();
      }
    }

    int answer = heap.top();

    return answer;
  }
};
