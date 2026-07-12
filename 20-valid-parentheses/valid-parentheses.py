class Solution:
    def isValid(self, s: str) -> bool:
        brac = ["(","{","["]
        lis = []

        for i in s:

            if i in brac:
                lis.append(i)
            else:
                if len(lis)==0:
                    return False
                if (lis[-1]=='(' and i==')') or (lis[-1]=='{' and i=='}') or (lis[-1]=='[' and i==']'):
                    lis.pop()
                else:
                    return False
        return len(lis)==0