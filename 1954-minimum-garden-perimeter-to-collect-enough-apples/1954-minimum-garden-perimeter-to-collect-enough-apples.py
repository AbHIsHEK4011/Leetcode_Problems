class Solution(object):
    def minimumPerimeter(self, neededApples):
        """
        :type neededApples: int
        :rtype: int
        """
        def calculate_apples(x):
            return (2 * x**2 + 2 * x) * (2 * x + 1)

        left, right = 1, 10 ** 6

        while left < right:
            mid = (left + right) // 2
            apples = calculate_apples(mid)

            if apples < neededApples:
                left = mid + 1
            else:
                right = mid

        return left * 8
        