class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        for i in range(0,len(nums)):
            l.append(nums[nums[i]])
        return l
            
        