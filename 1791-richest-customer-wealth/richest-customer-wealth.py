class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        result = []
        for wealths in accounts:
            result.append(sum(wealths))
        return max(result)