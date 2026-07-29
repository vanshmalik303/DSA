class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = []

        count=0
        for i in s:
            while i in check:

             check.pop(0)          # Remove from the left

            check.append(i)          # Add current character
            count = max(count, len(check))

        return count