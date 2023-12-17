class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        l= sentence.split()
        for i,j in enumerate(l,0):
            if j.startswith(searchWord):
                return i+1
        return-1
        