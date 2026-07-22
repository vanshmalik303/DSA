class Solution:
    def longestValidParentheses(self, s: str) -> int:
        result = [-1]
        ans = 0
        for i in range(len(s)):
            if s[i]=='(':
                result.append(i)
            else:
                result.pop()

                if not result:
                    result.append(i)
                else:
                    ans = max(ans, i - result[-1])

        return ans