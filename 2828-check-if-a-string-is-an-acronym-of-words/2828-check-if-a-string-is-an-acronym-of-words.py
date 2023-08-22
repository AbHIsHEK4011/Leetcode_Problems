class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        l=""
        for i in words:
            l+=i[0]
        return l==s