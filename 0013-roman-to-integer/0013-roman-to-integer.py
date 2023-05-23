class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman={'I':1,'V':5,'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        curr_val=0
        total=0
        prev_val=0
        for i in range(len(s)-1,-1,-1):
            curr_val= roman[s[i]]
            if curr_val>=prev_val:
                total+=curr_val
            else:
                total-=curr_val
            prev_val= curr_val
        return total