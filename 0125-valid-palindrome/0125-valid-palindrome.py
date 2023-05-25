class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str= re.sub('[^a-zA-Z0-9]','',s.lower())
        
        if str==str[::-1]:
            return True
        else:
            return False
        