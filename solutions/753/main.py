class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        # need to start with "0"*(n-1), not "0"*n
        ans = "0"*(n-1)
        my_map = {}
        for i in range(k**n): 
            # note the index is len(ans)-(n-1), not -(n-1)
            key = ans[len(ans)-(n-1):]
            my_map[key] = (my_map.get(key, 0)+1)%k
            ans += str(my_map[key])
        return ans 

if __name__ == "__main__": 
    s = Solution() 

    assert s.crackSafe(1, 3) == "120"
    # assert s.crackSafe(1, 2) == "01"