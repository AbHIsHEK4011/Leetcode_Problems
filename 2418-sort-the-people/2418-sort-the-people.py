class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        
        hash = {}
        for i in range(len(heights)):
            hash[heights[i]] = names[i]
        heights.sort(reverse=True)
        
        arr = []
        for i in heights:
            arr.append(hash[i])
        return arr
                
        