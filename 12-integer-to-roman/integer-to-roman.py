class Solution:
    def intToRoman(self, num: int) -> str:

        value = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        keys = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]

        lis = []
        # for number in range(len(value)-1):
        #     if value[number]<num and (value[number+1]>num or value[number+1]==Null):
        #         print(value[number])
        i = len(value)-1
        while num>0:
            if value[i]<=num:
                num=num-value[i]
                lis.append(keys[i])
            else:
                i-=1

        ans = (''.join(map(str,lis)))
        return ans