class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(0, len(s)-1):
            if s[i] == '0' and s[i+1] == '1':
                return False
        return True