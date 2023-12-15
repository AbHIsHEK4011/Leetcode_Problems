class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        a= int("".join(map(str,num)))
        i= a+k
        return [int(j) for j in str(i)]
        
        