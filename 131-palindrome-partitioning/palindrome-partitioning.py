class Solution:
    def partition(self, s: str) -> list[list[str]]:
        curr = []
        ans = []
        def f (i):
            if i==len(s):
                ans.append(curr.copy())
                return 
            for j in range(i,len(s)):
                part = s[i:j+1]
                if part == part[::-1]:
                    curr.append(part)
                    f(j+1)
                    curr.pop()
        f(0)
        return ans