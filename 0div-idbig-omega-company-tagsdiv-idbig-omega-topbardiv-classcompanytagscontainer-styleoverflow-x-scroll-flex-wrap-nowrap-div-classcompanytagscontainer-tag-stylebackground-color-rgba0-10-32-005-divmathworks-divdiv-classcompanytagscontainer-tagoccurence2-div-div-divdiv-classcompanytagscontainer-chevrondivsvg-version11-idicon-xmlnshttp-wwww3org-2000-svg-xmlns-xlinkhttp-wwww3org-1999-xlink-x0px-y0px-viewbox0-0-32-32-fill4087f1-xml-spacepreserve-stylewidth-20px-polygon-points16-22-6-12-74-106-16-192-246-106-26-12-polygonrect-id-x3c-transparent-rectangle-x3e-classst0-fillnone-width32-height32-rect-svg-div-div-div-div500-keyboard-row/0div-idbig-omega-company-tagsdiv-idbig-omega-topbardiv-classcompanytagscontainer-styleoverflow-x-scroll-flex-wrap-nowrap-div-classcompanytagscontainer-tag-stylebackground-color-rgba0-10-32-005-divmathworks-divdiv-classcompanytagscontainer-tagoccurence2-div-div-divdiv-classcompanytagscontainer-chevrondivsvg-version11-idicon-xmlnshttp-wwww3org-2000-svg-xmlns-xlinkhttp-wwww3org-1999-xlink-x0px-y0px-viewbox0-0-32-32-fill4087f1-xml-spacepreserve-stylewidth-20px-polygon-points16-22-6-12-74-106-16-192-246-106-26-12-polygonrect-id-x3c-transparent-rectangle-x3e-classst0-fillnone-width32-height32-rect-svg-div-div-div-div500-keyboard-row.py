class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        rows = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]

        for word in words:
            a = set(word.lower())
            if any(a <= row for row in rows):
                ans.append(word)
        return ans