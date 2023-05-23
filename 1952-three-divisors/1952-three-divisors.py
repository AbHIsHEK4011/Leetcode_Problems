class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        l=[]
        l.append(n)
        for i in range(1,n/2+1):
            if (n%i==0):
                l.append(i)
            
        if len(l)==3:
            return True
        else:
            return False
                