class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows,cols=len(grid), len(grid[0])
        res=0
        
        for i in range(rows):
            grid[i].sort()
        for j in range(cols):
            res+= max(grid[i][j] for i in range(rows))
        return res
            
        