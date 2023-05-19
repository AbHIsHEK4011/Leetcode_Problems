class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = list(set(nums))
        s.sort()
        return s[-3] if len(s) >= 3 else s[-1]


        

