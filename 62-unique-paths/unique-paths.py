class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[-1]*n for _ in range(m)]
        def f(i,j):
            if i>= m or j>=n:
                return 0
            if i==m-1 and j==n-1:
                return 1
            if dp[i][j] != -1:
                return dp[i][j]

            dp[i][j]= f(i+1,j)+f(i,j+1)
            return dp[i][j]

        return f(0,0)
