class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        l=[]
        for i in words:
            l.append(i[0])
        p=''.join(l)
        if p==s:
            return True
        else:
            return False