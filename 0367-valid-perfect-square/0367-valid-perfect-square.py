class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        h= math.sqrt(num)
        return h.is_integer()
        