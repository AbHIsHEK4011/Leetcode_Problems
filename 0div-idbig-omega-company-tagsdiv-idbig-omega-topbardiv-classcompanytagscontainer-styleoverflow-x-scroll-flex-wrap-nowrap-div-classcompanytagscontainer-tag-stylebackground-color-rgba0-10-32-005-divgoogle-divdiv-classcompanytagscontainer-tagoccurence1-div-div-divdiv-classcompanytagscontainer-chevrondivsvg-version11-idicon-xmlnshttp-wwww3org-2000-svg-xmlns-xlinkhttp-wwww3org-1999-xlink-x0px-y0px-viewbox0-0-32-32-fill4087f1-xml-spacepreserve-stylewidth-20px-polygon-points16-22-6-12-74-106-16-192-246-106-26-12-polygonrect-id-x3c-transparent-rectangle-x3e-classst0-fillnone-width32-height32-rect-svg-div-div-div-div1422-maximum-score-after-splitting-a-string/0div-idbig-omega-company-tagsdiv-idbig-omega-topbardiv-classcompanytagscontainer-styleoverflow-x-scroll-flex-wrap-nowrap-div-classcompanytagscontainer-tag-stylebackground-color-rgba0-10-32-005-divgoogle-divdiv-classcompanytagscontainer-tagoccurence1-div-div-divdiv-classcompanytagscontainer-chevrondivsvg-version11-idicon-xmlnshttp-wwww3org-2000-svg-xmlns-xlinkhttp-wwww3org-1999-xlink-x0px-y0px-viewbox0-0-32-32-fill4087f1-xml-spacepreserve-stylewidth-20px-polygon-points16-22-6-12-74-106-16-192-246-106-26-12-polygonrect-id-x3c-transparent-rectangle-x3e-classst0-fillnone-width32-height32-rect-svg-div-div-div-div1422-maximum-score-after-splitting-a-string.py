class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        zero= 0
        ones= s.count("1")
        for i in range(len(s)-1):
            if s[i]=="0":
                zero+=1
            else:
                ones-=1
            res = max(res,zero+ones)
        return res
        