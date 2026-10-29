class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        n = len(graph)
        ans = []
        path = []

        def dfs(node):
            path.append(node)

            if node == n - 1:
                ans.append(path.copy())
            else:
                for nei in graph[node]:
                    dfs(nei)

            path.pop()

        dfs(0)
        return ans