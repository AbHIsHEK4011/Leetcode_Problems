class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        for k in nums:
            j=str(k)
            for i in range(len(j)):
                l.append(int(j[i]))
                
        return l
                
                
        