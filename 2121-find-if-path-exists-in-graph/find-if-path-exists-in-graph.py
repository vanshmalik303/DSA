class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        adj = [[] for _ in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        result = []
        visited = [0]*n
        def dfs(node):

            result.append(node)
            visited[node]=1
            
            for n in (adj[node]):
                
                if visited[n]==0:
                    dfs(n)

        dfs(source)
        if visited[destination] ==1:
                return True
        else:
            return False
            

            