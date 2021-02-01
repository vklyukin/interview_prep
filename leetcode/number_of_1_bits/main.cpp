class Solution {
 public:
  bool isOdd(uint32_t n) { return n % 2 == 1; }

  int hammingWeight(uint32_t n) {
    int ones_count = 0;

    while (n > 0) {
      if (isOdd(n)) {
        ++ones_count;
      }
      n >>= 1;
    }

    return ones_count;
  }
};