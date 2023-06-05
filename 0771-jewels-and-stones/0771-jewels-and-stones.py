class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        j= set(jewels)
        k=0
        for s in stones:
            if s in j:
                k+=1
        return k