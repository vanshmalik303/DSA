class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        curr = []
        ans = []
        def f(i):

            if i == len(s):
                ans.append("".join(curr))
                return

            if s[i].isalpha():
                
                curr.append(s[i].lower())
                f(i+1)
                curr.pop()

                curr.append(s[i].upper())
                f(i+1)
                curr.pop()
            else:
                curr.append(s[i])
                f(i+1)
                curr.pop()
        f(0)
        return ans