class Solution:
    def countOdds(self, low: int, high: int) -> int:
        n= high-low+1
        return n//2 +   (1 if (low%2 and high%2) else 0)