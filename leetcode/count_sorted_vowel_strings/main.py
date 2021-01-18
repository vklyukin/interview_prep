class Solution:
    def __init__(self):
        self.count_memo = {}

    def countPossibleVariations(self, previous_char, current_index, total_length):
        key = (previous_char, current_index, total_length)
        if key in self.count_memo:
            return self.count_memo[key]

        if current_index == total_length:
            self.count_memo[key] = 1
            return 1

        current_step_answer = 0
        for possible_char in range(previous_char, 5):
            current_step_answer += self.countPossibleVariations(
                possible_char, current_index + 1, total_length
            )

        self.count_memo[key] = current_step_answer
        return current_step_answer

    def countVowelStrings(self, n: int) -> int:
        return self.countPossibleVariations(0, 0, n)
