from typing import List 

class Solution:
    # ref https://leetcode-cn.com/problems/zigzag-conversion/solution/zzi-xing-bian-huan-by-jyd/
    def convert(self, s: str, numRows: int) -> str:
        # check input
        if numRows == 1:
            return s
        result = ["" for _ in range(numRows)]
        i = 0
        flag = -1
        for c in s:
            result[i] += c
            if i == 0 or i == numRows-1:
                flag *= -1
            i += flag
        return "".join(result)

if __name__ == "__main__": 
    s = "PAYPALISHIRING"
    numRows = 3
    ans = "PAHNAPLSIIGYIR"
    sol = Solution()
    assert sol.convert(s, numRows) == ans 

