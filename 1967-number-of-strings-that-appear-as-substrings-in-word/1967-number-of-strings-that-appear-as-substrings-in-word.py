class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        k=0
        for i in patterns:
            if i in word :
                k+=1
        return k
        