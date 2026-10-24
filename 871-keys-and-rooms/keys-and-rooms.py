class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        n = len(rooms)
        visited  = [0]*n
        result = []

        def dfs(node):
            nonlocal n
            result.append(node)
            visited[node] = 1

            for nebi in rooms[node]:
                
                if visited[nebi]==0:
                    dfs(nebi)
        dfs(0 )
        return len(result)==n
        