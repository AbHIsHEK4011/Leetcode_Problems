class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for l in s:
            if len(stack) > 0 and ((stack[-1] == 'A' and l == 'B') or (stack[-1] == 'C' and l == 'D')):
                stack.pop()
            else:
                stack.append(l)
        return len(stack)
        