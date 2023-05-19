class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        dic={}
        for num in arr:
            if num not in dic:
                dic[num]=1
            else:
                dic[num]+=1
        x= int(math.ceil(len(arr)/4))
        for nums,freq in dic.items():
            if freq>x:
                return nums
        
        