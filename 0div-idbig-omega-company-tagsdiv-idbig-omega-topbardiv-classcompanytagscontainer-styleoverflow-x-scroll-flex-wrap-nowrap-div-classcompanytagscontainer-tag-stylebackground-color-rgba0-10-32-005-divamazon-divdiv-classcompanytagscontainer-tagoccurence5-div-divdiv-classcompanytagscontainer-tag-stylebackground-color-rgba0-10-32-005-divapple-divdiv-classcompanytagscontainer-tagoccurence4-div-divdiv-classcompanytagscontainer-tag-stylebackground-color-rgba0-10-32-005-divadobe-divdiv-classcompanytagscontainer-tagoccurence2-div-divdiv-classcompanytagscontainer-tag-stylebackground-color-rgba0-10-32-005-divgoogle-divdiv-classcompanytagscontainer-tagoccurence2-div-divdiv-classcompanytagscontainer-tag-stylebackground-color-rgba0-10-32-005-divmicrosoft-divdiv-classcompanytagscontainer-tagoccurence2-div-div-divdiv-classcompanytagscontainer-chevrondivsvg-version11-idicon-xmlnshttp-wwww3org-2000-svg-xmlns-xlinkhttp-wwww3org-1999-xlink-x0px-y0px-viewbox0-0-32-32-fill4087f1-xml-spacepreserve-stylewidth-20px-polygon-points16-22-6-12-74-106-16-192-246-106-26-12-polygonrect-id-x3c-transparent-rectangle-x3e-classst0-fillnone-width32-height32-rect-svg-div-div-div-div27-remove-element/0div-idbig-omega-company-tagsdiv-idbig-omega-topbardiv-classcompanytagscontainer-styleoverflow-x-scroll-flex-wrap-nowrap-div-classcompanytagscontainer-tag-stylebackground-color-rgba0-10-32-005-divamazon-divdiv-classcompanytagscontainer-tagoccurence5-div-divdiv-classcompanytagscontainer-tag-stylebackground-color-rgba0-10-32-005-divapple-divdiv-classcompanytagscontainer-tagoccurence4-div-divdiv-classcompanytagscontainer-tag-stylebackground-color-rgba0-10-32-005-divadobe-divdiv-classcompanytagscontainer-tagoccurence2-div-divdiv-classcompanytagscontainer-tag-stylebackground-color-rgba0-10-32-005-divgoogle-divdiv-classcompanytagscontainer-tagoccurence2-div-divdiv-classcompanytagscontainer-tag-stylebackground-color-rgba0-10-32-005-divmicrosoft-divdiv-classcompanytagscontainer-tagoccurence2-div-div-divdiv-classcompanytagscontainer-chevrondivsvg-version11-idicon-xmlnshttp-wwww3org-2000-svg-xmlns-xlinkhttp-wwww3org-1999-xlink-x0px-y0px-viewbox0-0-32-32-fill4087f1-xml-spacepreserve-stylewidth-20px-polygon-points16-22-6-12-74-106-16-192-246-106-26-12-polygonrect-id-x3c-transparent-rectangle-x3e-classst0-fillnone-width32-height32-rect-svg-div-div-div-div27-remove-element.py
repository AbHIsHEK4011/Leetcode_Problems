class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l=0
        for right in range(len(nums)):
            if nums[right] != val:
                nums[l] = nums[right]
                l += 1
        return l
                
        