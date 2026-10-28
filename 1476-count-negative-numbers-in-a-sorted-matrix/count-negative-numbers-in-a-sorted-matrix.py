class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        result = []
        for i in grid :
            for j in i:
                if j<0:
                    result.append(j)
        return len(result)
