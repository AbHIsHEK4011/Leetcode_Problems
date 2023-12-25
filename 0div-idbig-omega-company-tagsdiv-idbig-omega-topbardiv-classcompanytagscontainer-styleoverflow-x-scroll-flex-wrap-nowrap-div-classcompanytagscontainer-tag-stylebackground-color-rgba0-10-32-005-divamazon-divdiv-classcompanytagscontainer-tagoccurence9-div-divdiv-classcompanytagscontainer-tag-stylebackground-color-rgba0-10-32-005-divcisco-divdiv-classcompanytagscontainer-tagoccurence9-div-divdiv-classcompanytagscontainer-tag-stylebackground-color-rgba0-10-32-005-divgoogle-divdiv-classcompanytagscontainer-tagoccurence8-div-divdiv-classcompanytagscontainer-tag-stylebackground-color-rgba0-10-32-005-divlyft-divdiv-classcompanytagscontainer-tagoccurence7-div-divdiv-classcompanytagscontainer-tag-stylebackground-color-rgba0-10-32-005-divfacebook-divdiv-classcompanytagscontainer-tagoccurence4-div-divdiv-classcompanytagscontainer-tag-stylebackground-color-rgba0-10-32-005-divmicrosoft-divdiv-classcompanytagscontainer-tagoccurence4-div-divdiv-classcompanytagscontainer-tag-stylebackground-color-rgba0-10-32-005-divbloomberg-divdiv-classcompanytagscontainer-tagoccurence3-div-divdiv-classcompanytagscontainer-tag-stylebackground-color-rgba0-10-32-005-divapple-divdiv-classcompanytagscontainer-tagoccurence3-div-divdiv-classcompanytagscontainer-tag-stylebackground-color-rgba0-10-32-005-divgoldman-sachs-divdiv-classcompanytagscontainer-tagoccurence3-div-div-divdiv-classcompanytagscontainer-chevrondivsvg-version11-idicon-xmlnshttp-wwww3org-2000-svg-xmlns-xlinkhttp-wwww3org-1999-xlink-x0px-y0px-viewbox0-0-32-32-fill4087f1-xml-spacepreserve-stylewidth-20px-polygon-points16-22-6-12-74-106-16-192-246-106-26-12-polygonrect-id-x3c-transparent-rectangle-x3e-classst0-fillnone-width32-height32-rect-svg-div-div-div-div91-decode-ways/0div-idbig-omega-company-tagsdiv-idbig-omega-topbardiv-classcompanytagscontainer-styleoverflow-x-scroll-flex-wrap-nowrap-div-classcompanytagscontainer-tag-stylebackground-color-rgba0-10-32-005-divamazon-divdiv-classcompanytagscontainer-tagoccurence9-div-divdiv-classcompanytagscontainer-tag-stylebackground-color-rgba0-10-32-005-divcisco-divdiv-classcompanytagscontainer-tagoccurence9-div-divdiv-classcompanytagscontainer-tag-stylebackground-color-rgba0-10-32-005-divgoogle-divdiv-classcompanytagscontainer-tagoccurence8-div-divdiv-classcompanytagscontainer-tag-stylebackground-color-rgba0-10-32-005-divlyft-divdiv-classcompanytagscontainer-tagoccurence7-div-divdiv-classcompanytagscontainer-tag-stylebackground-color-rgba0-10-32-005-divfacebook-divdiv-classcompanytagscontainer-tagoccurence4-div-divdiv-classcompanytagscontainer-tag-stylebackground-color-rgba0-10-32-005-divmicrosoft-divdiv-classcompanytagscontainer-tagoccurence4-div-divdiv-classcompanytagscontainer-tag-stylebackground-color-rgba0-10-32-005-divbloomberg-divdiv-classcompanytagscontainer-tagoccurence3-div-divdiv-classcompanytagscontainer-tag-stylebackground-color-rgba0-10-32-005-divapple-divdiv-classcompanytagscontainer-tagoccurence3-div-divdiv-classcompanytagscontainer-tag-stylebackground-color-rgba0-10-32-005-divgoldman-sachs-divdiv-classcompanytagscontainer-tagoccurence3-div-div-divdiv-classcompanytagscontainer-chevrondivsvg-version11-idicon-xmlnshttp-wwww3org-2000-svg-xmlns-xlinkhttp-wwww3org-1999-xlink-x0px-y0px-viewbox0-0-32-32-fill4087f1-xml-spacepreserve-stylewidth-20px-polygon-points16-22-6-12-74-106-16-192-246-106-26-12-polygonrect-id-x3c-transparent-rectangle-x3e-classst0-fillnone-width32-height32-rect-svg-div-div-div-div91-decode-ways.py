class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [0] * n + [1]
        def fun1(a, b=None):
            if b:
                return a == '1' or a == '2' and b < '7'
            return a != '0'

        if fun1(s[-1]):
            dp[n - 1] = 1

        for i in reversed(range(n - 1)):
            if fun1(s[i]):
                dp[i] += dp[i + 1]
            if fun1(s[i], s[i + 1]):
                dp[i] += dp[i + 2]

        return dp[0]
    
        