from collections import deque
class Solution:
    def findShortestCycle(self, n: int, edges: list[list[int]]) -> int:

        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        ans = float('inf')

        for start in range(n):

            dist = [-1] * n
            parent = [-1] * n

            q = deque([start])
            dist[start] = 0

            while q:
                node = q.popleft()

                for nei in adj[node]:

                    if dist[nei] == -1:
                        dist[nei] = dist[node] + 1
                        parent[nei] = node
                        q.append(nei)

                    elif parent[node] != nei:
                        cycle = dist[node] + dist[nei] + 1
                        ans = min(ans, cycle)

        if ans == float('inf'):
            return -1

        return ans
        # adj = [[] for _ in range(n)]

        # for u,v in edges:
        #     adj[u].append(v)
        #     adj[v].append(u)
        
        # result = []
        # visited = [0]*n
        # iscycle = False
        # def dfs(node,parent):
        #     nonlocal iscycle
        #     visited[node]=1
        #     result.append(node)
        #     for i in adj[node]:
        #         if visited[i]==0:
        #             dfs(i,node)  
        #         elif i != parent:
        #             iscycle = True
                    

        # ans = []
        # for i in range(n):
        #     if visited[i] ==0:
        #         dfs(i,i)
        #         ans.append(result)
                
        #         result =[]
        # # if len(ans)
        # if iscycle == False:
        #     return -1
        # else:
        #     print(ans)
        #     # return(len(min(ans)))

        




        # dist = [-1]*n
        # def bfs(node):
        #     queue = deque([node])
        #     dist[node]=1
        #     while queue:
        #         e = queue.popleft()
        #         for i in adj[node]:
        #             if dist[i]==-1:
        #                 queue.append(i)
        #                 dist[i]=1
        # return dist
        # bfs(node)
        # for i in range(n):
        #     if dist[i]==-1:
        #         queue.append(i)
