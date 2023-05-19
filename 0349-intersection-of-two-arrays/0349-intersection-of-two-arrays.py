class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s=set()
        s1=set()
        for i in nums1:
            s.add(i)
        for i in nums2:
            s1.add(i)
        l=[]
        for i in s:
            for j in s1:
                if(i==j):
                    l.append(i)
        return l
