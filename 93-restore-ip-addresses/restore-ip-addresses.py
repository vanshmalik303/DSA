class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:

        curr = []
        ans = []

        def f(i):

            if len(curr)==4:
                if i==len(s):
                    ans.append(".".join(curr.copy()))
                    return

            for j in range(i,min((i+3),len(s))):
                part = s[i:j+1]
                if int(part)<0 or int(part)>255: 
                    continue
                if len(part) != 1 and part[0]=='0':
                    continue
                curr.append(part)
                f(j+1)
                curr.pop()
        f(0)
        return ans
