class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) > len(b):
            b = "0" * (len(a) - len(b)) + b
        else:
            a = "0" * (len(b) - len(a)) + a
        ans = ""
        inc = 0
        for i in range(max(len(a), len(b)) - 1, -1, -1):
            ans = str((int(a[i]) + int(b[i]) + int(inc)) % 2) + ans
            if int(a[i]) + int(b[i]) + int(inc) > 1:
                inc = 1
            else:
                inc = 0
        if inc == 1:
            ans = "1" + ans
        return ans