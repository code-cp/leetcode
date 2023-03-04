class Solution:
    def printBin(self, num: float) -> str:
        res = "0."
        while len(res) <= 32 and num > 0: 
            # 在二进制表示中，将一个数乘以 2 的效果是将小数点向右移动一位
            num *= 2 
            digit = int(num)
            res += str(digit)
            num -= digit 
        return res if len(res) <= 32 else "ERROR"