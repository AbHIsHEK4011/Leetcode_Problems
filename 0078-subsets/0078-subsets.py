class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        a=[]
        def s(i):
            if i==len(nums):
                l=list(a)
                res.append(l)
                return
            a.append(nums[i])
            s(i+1)
            a.pop()
            s(i+1)
        s(0)
        return res
            
        