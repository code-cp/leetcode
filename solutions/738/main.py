from typing import List 

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        strNum = list(str(n))
        for i in range(len(strNum)-1, 0, -1):
            if int(strNum[i-1]) > int(strNum[i]):
                strNum[i-1] = str(int(strNum[i-1]) - 1)
                strNum[i:] = '9' * (len(strNum) - i)
        return int("".join(strNum))

if __name__ == "__main__":
    n = 10
    s = Solution()
    assert s.monotoneIncreasingDigits(n) == 9
