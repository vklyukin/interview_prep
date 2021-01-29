import string


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        string_code = []

        while n > 0:
            max_letter_code = min(26, k - n + 1)
            string_code.append(max_letter_code)

            n -= 1
            k -= max_letter_code

        smallest_string = "".join(
            string.ascii_lowercase[index - 1] for index in reversed(string_code)
        )

        return smallest_string
