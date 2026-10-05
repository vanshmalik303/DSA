class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        count = []
        ans = []

        def f(candi,target):
            if target==0:
                ans.append(count.copy())
                return
            if target<0:
                return
            for i in range(candi,len(candidates)):
                count.append(candidates[i])
                f(i,target-candidates[i])
                count.pop()
        f(0,target)
        return ans