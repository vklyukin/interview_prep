class Solution:
    def reverseString(self, s):
        buf = ""

        for i in range(len(s) - 1, -1, -1):
            buf += s[i]

        return buf