class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        exp=sorted(heights)
        sum1=0
        for i in range(len(heights)):
            if heights[i] != exp[i]:
                sum1+=1
        return sum1

                
            