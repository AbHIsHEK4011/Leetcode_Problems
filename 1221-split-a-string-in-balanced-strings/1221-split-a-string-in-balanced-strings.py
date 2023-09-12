class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = l = 0
        for i in s:
            if i == 'L':
                l += 1
            else:
                l -= 1
            if l == 0:
                res += 1
        return res