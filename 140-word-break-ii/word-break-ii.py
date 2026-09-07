class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        curr = []

        def f(index):
            if index == len(s):
                ans.append(" ".join(curr))

            for j in range(index, len(s)+1):
                word = s[index: j+1]
                if word in wordDict:
                    curr.append(word)
                    f(j+1)
                    curr.pop()
        f(0)
        return ans