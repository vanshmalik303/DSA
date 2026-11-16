class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[-1]*m for _ in range(n)]
        def solve(i,j):
            if i==len(text1) or j==len(text2):
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if text1[i]==text2[j]:
                dp[i][j]= 1+solve(i+1,j+1)
            else:
                dp[i][j]= max(solve(i+1,j),solve(i,j+1))
            return dp[i][j]
        
        return solve(0,0)