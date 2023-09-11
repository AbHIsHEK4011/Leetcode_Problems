class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtyres.appendpe: List[int]
        """
        if not nums1 or not nums2:
            return []
        map1= collections.Counter(nums1)
        res=[]
        for num in nums2:
            if num in map1 and map1[num]:
                res.append(num)
                map1[num]-=1
        return res
                
            
                
        