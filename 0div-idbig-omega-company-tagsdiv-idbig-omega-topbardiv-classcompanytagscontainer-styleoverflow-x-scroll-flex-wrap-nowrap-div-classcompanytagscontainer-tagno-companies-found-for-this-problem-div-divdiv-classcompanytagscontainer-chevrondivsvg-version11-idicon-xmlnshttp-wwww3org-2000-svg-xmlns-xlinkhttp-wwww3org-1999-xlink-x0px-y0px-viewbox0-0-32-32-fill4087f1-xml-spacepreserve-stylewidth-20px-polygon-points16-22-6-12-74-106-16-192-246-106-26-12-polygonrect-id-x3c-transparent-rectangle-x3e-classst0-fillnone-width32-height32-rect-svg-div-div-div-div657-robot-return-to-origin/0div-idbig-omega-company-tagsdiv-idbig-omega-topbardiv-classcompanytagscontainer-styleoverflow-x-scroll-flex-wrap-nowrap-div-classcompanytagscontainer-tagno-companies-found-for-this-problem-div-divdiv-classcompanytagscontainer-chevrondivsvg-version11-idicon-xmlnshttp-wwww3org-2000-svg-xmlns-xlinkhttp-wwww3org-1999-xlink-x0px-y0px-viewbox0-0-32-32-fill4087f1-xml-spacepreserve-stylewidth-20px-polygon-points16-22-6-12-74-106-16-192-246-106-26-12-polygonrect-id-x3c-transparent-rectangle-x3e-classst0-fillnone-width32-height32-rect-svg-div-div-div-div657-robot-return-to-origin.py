class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        a=[0,0]
        for i in moves:
            if i=="U":
                a[1]+=1
            if i=="D":
                a[1]-=1
            if i=="R":
                a[0]+=1
            if i=="L":
                a[0]-=1
        if a[0]==0 and a[1]==0:
            return True
        else:
            return False
        