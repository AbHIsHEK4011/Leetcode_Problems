class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums.sort()
        mis = len(nums)
        for i in range(len(nums)):
            
            mis ^= i^nums[i]
        return mis
        