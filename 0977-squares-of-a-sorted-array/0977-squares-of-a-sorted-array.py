class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        start=0
        
        end= len(nums)-1
        while start<=end:
            if start!=end:
                nums[start]= nums[start]**2
                nums[end]= nums[end]**2
            else:
                nums[start]= nums[start]**2
            start+=1
            end-=1
        nums.sort()
        return nums
        