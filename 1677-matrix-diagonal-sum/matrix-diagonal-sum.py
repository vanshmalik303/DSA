class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        n = len(mat)
        result = []
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i==j or i+j==n-1:

                    result.append(mat[i][j])
        return sum(result)
        