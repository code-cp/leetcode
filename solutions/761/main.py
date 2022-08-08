class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        def dfs(sbs):
            res = []
            i, height = 0, 0
            for j in range(len(sbs)): 
                if sbs[j] == '1':
                    height += 1 
                else: 
                    height -= 1 
                if height == 0: 
                    sub = '1' + dfs(sbs[i+1:j]) + '0'
                    res.append(sub)
                    i = j+1 
            res.sort(reverse=True)
            return "".join(res)
        res = dfs(s)
        return res 


if __name__ == "__main__": 
    sol = Solution()

    s = "11011000"
    assert sol.makeLargestSpecial(s) == "11100100"