class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic={}
        for num in nums:
            if num not in dic:
                dic[num]=1
            else:
                dic[num]+=1 
        for count in dic.values():
            if count>1:
                return True
        return False
