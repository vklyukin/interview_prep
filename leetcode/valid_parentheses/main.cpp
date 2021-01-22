class Solution {
 public:
  bool isValid(string s) {
    vector<char> char_stack;

    for (char s_char : s) {
      if (s_char == '(' || s_char == '[' || s_char == '{') {
        char_stack.push_back(s_char);
      } else if (s_char == ')') {
        if (char_stack.empty() || char_stack.back() != '(') {
          return false;
        }
        char_stack.pop_back();
      } else if (s_char == ']') {
        if (char_stack.empty() || char_stack.back() != '[') {
          return false;
        }
        char_stack.pop_back();
      } else if (s_char == '}') {
        if (char_stack.empty() || char_stack.back() != '{') {
          return false;
        }
        char_stack.pop_back();
      }
    }

    return char_stack.empty();
  }
};
