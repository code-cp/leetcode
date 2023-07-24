class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0 
        jewels_set = set()
        for j in jewels: 
            jewels_set.add(j)
        cnt = Counter(stones)
        for k, v in cnt.items():
            # print(f"k {k} v {v}") 
            if k in jewels_set: 
                ans += v 
        return ans