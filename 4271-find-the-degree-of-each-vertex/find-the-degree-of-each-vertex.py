class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        curr = []
        for i in matrix:
            curr.append(sum(i))

        return(curr)