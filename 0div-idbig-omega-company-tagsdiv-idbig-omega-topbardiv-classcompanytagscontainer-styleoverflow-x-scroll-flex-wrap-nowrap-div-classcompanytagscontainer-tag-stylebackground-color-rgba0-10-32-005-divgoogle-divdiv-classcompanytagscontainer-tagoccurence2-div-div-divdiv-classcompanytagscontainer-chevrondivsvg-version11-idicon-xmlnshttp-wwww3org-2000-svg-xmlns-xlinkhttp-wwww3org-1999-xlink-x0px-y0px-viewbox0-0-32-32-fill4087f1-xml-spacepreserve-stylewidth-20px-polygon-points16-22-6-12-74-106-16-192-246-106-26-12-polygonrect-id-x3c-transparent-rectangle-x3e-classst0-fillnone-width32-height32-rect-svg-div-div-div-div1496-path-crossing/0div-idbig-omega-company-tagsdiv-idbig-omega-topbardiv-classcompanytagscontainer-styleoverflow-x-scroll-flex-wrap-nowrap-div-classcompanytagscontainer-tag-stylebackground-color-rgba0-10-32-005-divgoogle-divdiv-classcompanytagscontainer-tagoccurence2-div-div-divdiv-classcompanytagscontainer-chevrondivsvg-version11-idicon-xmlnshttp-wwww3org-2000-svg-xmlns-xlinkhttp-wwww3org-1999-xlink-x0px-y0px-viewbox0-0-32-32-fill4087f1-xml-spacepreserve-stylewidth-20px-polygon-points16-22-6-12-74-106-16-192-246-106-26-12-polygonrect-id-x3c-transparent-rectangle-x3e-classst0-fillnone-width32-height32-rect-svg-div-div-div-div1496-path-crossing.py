class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        s={
            "N": [0,1],
            "S": [0,-1],
            "E": [1,0],
            "W": [-1,0]
        }
        v=set()
        x,y=0,0
        for i in path:
            v.add((x,y))
            a,b=s[i]
            x,y=x+a,y+b
            if (x,y) in v:
                return True
        return False
            
        