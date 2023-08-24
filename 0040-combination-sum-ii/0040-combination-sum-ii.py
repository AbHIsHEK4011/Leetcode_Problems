class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def com_sum(candidates,target,index,a,res):
            if target==0 :
                res.append(list(a))
                return
            for i in range(index,len(candidates)):
                if i>index and candidates[i-1]==candidates[i]:
                    continue
                if candidates[i]>target:
                    break
                a.append(candidates[i])
                com_sum(candidates,target-candidates[i],i+1,a,res)
                a.pop()
        a,res=[],[]
        candidates.sort()
        com_sum(candidates,target,0,a,res)
        return res
            
            
        