from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            '2':'abc',
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        ans = []
        for i in digits :
            ans.append(phone[i])

        lst = [''.join(p) for p in product(*ans)]
        return (lst)
