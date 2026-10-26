class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        result = []
        
        if len(original) != m*n:
            return []

        k = 0
        for i in range(m):
            arr = []
            for j in range(n):
                arr.append(original[k])
                k+=1
            result.append(arr.copy())

        return(result)
      