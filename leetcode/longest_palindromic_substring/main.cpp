class Solution {
 public:
  string longestPalindrome(const string& s) {
    int answer_start = 0;
    int answer_length = 0;

    int s_length = s.length();

    for (int center_index = 0; center_index < s_length; ++center_index) {
      int left_index = center_index;
      int right_index = center_index;

      while (left_index > -1 && right_index < s_length &&
             s[left_index] == s[right_index]) {
        int palindrome_length = right_index - left_index + 1;

        if (palindrome_length > answer_length) {
          answer_start = left_index;
          answer_length = palindrome_length;
        }

        --left_index;
        ++right_index;
      }
    }

    for (int center_index = 0; center_index + 1 < s_length; ++center_index) {
      int left_index = center_index;
      int right_index = center_index + 1;

      while (left_index > -1 && right_index < s_length &&
             s[left_index] == s[right_index]) {
        int palindrome_length = right_index - left_index + 1;

        if (palindrome_length > answer_length) {
          answer_start = left_index;
          answer_length = palindrome_length;
        }

        --left_index;
        ++right_index;
      }
    }

    return s.substr(answer_start, answer_length);
  }
};
