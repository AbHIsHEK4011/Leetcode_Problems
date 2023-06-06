class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        d = dict.fromkeys(string.ascii_lowercase, 0)
        for k in sentence:
            d[k]+=1
        for l in d.values():
            if l==0:
                return False
        return True

                
        