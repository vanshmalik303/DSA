class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        curr = []
        ans = []

        def f(start):

            if len(curr)==k:
                ans.append(curr.copy())
                return
            for i in range(start,n+1):
                curr.append(i)
                f(i+1)
                curr.pop()
        f(1)
        return ans