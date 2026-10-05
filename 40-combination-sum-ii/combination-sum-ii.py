class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:

        curr = []
        ans = []
        candidates.sort()
        def f(candi,target):
            if target==0 :
                ans.append(curr.copy())
                return 
            if target<0:
                return

            for i in range(candi,len(candidates)):
                if i>candi and candidates[i] == candidates[i-1]:
                    continue
                curr.append(candidates[i])
                f(i+1,target-candidates[i])
                curr.pop()
        f(0,target)
        return ans

