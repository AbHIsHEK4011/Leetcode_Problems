class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        start =0 
        end= int(math.sqrt(c))
        while start<=end:
            sum= start**2 + end**2
            if sum== c:
                return True
            elif sum<c:
                start+=1
            else:
                end-=1
        return False