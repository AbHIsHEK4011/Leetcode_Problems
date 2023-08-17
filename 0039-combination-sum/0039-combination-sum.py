class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def fun(index,candidates,target,a,res):
            if index==len(candidates):
                if target==0:
                    res.append(list(a))
                return
            if candidates[index]<=target:
                a.append(candidates[index])
                fun(index,candidates,target-candidates[index],a,res)
                a.pop()
            
            fun(index+1,candidates,target,a,res)
            
        res=[]
        fun(0,candidates,target,[],res)
        return res
        