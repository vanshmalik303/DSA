class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        visited = [[0] * m for _ in range(n)]

        def dfs(r, c):
            if r < 0 or r >= n or c < 0 or c >= m:
                return 0

            if grid[r][c] == 0 or visited[r][c] == 1:
                return 0

            visited[r][c] = 1

            area = 1

            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)

            return area

        ans = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    area = dfs(i, j)
                    ans = max(ans, area)

        return ans