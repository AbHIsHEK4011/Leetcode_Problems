class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        count= Counter(students)
        for i in sandwiches:
            if count[i]>0:
                count[i]-=1
            else:
                return count[not i]
        return 0