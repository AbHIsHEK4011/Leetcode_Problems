class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = int("".join([str(i) for i in digits]))
        re= res+1
        # print(re)
        ress= [int(x) for x in str(re)]
        return ress