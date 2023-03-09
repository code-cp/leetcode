class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        max_len = 0 
        cur_len = 0 
        for i in range(k): 
            if blocks[i] == "B": 
                cur_len += 1 
        max_len = max(max_len, cur_len)
        for i in range(k, len(blocks)):
            if blocks[i-k] == "B": 
                cur_len -= 1 
            if blocks[i] == "B": 
                cur_len += 1 
            max_len = max(max_len, cur_len)
        return max(0, k-max_len)
                  
        
if __name__ == "__main__": 
    s = Solution() 

    # blocks = "BWWWBB"
    # k = 6
    # assert s.minimumRecolors(blocks, k) == 3
    
    blocks = "WBBWWBBWBW"
    k = 7
    assert s.minimumRecolors(blocks, k) == 3