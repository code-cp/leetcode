from collections import Counter
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        cnt = Counter(tiles)
        letters = list(cnt.keys())
        cnt = list(cnt.values())
        ans = set()
        def dfs(cur, ans):
            ans.add(cur)
            # base case 
            if sum(cnt) == 0: 
                return 
            for i in range(len(cnt)): 
                if cnt[i] != 0: 
                    cnt[i] -= 1 
                    dfs(cur+letters[i], ans)
                    cnt[i] += 1 
        dfs("", ans)
        return len(ans) - 1 
    
if __name__ == "__main__": 
    s = Solution() 
    
    tiles = "AAB"
    assert s.numTilePossibilities(tiles) == 8 