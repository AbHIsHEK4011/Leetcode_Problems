class Solution(object):
    def findTheDifference(self, s, t):
        sum1=0
        sum2=0
        for i in t:
            sum1+=ord(i)
        for j in s:
            sum2+=ord(j)
        return chr(sum1-sum2)
        
            