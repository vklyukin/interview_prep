class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_id, t_id = 0, 0

        s_len, t_len = len(s), len(t)

        while t_id < t_len and s_id < s_len:

            if t[t_id] == s[s_id]:
                s_id += 1
                t_id += 1
            else:
                t_id += 1

        if s_id < s_len:
            return False
        else:
            return True
