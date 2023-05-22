class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        left=0
        boat=0
        right=len(people)-1
        people.sort()
        while left<=right:
            sum= people[left]+people[right]
            if sum<=limit:
                left += 1
                right -= 1
            else:
                right-=1
            boat+=1
        return boat
        