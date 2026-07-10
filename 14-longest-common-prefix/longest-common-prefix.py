class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]

        for i in range(len(first)):
            for j in range(1,len(strs)):
                if i>=len(strs[j]) or strs[j][i] != first[i]:
                    return first[:i]
        return first