class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        f={"}":"{",")":"(","]":"["}
        for a in s:
            if a in f:
                if stack and stack[-1]==f[a]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(a)
        return True if not stack else False
