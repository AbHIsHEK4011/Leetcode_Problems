class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        d=defaultdict(int)
        for w in words:
            for c in w:
                d[c]+=1
        for k in d:
            if d[k] % len(words):
                return False
        return True
        