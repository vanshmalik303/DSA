class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        curr = []
        ans = []

        
        def f(open,close):
                if len(curr)==2*n:
                    ans.append(''.join(curr))
                    return
                if open<n:
                    curr.append('(')
                    f(open+1,close)
                    curr.pop()
                if close<open:
                    curr.append(')')
                    f(open,close+1)
                    curr.pop()
        f(0,0)
        return ans