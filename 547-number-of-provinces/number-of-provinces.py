class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        result = []
        visited = [0]*n
        count = 0
        def dfs(node):
            result.append(node)
            visited[node]=1
            
            
            for nebighour in range(n):
                if isConnected[node][nebighour]==1:
                    if visited[nebighour]==0:
                        dfs(nebighour)
        for i in range(n):
            if visited[i]==0:
                dfs(i)
                count+=1
        return count
        