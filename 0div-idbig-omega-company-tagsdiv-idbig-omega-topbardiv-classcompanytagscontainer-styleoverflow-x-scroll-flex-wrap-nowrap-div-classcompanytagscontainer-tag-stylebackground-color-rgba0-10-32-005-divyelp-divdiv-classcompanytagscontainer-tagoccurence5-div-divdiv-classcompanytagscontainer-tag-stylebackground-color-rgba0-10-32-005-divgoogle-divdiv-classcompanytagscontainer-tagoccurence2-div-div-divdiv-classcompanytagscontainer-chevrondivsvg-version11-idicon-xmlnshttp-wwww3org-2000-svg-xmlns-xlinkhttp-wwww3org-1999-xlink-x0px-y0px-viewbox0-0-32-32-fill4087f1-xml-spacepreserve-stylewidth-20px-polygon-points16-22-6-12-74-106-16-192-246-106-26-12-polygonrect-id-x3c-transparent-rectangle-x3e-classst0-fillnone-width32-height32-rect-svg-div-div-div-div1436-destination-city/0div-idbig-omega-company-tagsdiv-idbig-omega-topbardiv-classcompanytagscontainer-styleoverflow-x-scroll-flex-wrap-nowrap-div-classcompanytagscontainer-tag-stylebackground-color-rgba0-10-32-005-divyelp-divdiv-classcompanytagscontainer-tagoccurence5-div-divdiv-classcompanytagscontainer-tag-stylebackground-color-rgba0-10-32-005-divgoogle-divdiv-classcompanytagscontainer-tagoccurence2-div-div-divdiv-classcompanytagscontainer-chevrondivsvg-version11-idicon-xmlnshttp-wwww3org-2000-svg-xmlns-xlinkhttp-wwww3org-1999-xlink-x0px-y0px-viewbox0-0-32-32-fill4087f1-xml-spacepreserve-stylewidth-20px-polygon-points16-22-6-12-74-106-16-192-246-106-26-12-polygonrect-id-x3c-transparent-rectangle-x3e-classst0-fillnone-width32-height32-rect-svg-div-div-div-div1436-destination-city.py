class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        s=set()
        for i in paths:
            s.add(i[0])
        for i in paths:
            if i[1] not in s:
                return i[1]
        