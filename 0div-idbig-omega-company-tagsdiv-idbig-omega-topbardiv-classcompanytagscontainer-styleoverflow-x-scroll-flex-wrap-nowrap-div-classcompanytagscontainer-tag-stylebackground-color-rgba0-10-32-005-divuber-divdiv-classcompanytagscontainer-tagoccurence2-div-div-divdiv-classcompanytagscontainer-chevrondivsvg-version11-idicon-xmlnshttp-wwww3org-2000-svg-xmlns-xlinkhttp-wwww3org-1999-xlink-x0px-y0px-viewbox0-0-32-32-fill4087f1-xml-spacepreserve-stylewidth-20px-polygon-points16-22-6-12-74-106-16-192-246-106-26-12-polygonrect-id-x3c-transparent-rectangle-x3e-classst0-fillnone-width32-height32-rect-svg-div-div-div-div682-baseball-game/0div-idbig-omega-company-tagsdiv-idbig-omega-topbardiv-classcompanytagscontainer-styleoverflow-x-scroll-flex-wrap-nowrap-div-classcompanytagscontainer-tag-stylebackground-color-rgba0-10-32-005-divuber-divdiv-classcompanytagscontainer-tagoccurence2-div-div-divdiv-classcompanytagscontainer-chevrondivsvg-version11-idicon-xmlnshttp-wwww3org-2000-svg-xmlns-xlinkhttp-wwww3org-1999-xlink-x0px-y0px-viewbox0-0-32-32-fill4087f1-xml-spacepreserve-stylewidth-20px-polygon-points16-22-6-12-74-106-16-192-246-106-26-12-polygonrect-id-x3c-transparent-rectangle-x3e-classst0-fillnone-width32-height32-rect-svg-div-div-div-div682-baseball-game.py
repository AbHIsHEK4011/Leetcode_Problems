class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        l = []
        i=0
        while i<len(operations):
            if operations[i]!= "C" and operations[i]!= "D" and operations[i]!= "+":
                l.append(int(operations[i]))
            elif operations[i]=="C":
                l.remove(l[-1])
            elif operations[i] == "D":
                l.append(l[-1]*2)
            elif operations[i] == "+":
                l.append(l[-1] + l[-2])
            i+=1
        return (sum(l))
        