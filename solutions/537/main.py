class Solution:
    @staticmethod
    def str2comp(num): 
        num = num.split("+")
        real = int(num[0])
        imag = int(num[1][:-1])
        return real, imag
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real1, imag1 = self.str2comp(num1)
        real2, imag2 = self.str2comp(num2)
        real = real1 * real2 + -1 * (imag1 * imag2)
        imag = real1 * imag2 + real2 * imag1 
        result = str(real) + "+" + str(imag) + "i"
        return result

if __name__ == "__main__": 
    s = Solution()
    num1 = "1+-1i"
    num2 = "1+-1i" 
    result = s.complexNumberMultiply(num1, num2)
    assert result == "0+-2i"
