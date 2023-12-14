class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n= len(nums)
        sum_nums= sum(nums)
        abs_nums= sum(set(nums))
        duplicate= sum_nums - abs_nums
        missing = (n*(n+1))//2 - abs_nums
        return [duplicate, missing]