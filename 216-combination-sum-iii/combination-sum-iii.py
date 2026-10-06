class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        curr = []
        ans = []

        def f(candi,n):
            if n==0 and len(curr)==k:
                ans.append(curr.copy())
                return
            if n<0:
                return

            for i in range(candi,10):
                curr.append(i)
                f(i+1,n-i)
                curr.pop()
        f(1,n)
        return ans