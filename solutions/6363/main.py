from typing import * 

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        # step1 construct 
        # step2 check 
        
        n = len(lcp)
        res = [""]*n
        next_char = "a"

        for i in range(n): 
            if res[i] == "":
                if next_char > "z": 
                    # no more alphabets available 
                    return ""
                # fill in next smallest char
                res[i] = next_char
                # fill in the same chars based on lcp 
                for j in range(i+1, n): 
                    if lcp[i][j] > 0: 
                        res[j] = res[i]
                next_char = chr(ord(next_char)+1)

        # if s[i] == s[j] => lcp[i][j] = lcp[i+1][j+1] + 1
        # if s[i] != s[j] => lcp[i][j] = 0
        for i in range(n): 
            if lcp[i][n-1] != (res[i] == res[n-1]):
                return ""
            if lcp[n-1][i] != (res[i] == res[n-1]):
                return ""
        for i in range(n-1):
            for j in range(n-1): 
                if res[i] == res[j]: 
                    if lcp[i][j] != lcp[i+1][j+1] + 1: 
                        return ""
                else: 
                    if lcp[i][j] != 0: 
                        return ""

        return "".join(res)


if __name__ == "__main__": 
    s = Solution() 

    lcp = [[2,0],[2,1]]
    assert s.findTheString(lcp) == ""

    # lcp = [[2,1],[2,1]]
    # assert s.findTheString(lcp) == ""

    # lcp = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]
    # assert s.findTheString(lcp) == "abab"