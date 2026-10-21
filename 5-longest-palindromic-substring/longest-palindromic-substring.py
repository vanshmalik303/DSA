class Solution:
    def longestPalindrome(self, s: str) -> str:

        ans = ""

        for i in range(len(s)):


            left = i
            right = i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(ans):
                    ans = s[left:right+1]

                left -= 1
                right += 1


            left = i
            right = i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(ans):
                    ans = s[left:right+1]

                left -= 1
                right += 1

        return ans


        # ans = []
        # for i in range(len(s)):
        #     for j in range(len(s)):
        #         part = s[i:j+1]
        #         if part == part[::-1]:
        #             ans.append(part)
        # return (max(ans,key=len))

        # curr = []
        # ans = []

        # def f(i):
        #     if i==len(s):
        #         ans.append(curr.copy())
        #         return 
        #     for j in range(i,len(s)):
        #         part = s[i:j+1]

        #         if part == part[::-1]:
                    
        #             curr.append(part)
        #             f(j+1)
        #             curr.pop()
        # f(0)
        # result = []

        # for i in ans:
        #     result.append(max(i,key=len))
        # return (max(result,key=len))