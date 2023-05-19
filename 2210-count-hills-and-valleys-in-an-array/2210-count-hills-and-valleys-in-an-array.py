class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=0
        for i in range(1,len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i-1]
            elif nums[i-1] > nums[i] < nums[i+1] or nums[i-1] < nums[i] > nums[i+1]:
                result += 1
        return result
            
        