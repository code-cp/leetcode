class Solution:
    @staticmethod
    def secMax(ls, m_idx): 
        sec_max = -float("inf")
        sec_idx = 0
        for i in range(len(ls)): 
            if i != m_idx and sec_max < ls[i]:
                sec_max = ls[i]
                sec_idx = i
        return sec_idx
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        alphabets = ["a", "b", "c"]
        ls = [a, b, c]
        result = ""
        count = 0
        idx = ls.index(max(ls))
        pre_idx = idx
        while True: 
            result += alphabets[idx]
            count += 1 
            ls[idx] -= 1 
            if ls[idx] == 0 or count == 2:
                idx = self.secMax(ls, idx) 
                if ls[idx] == 0 or pre_idx == idx: 
                    return result
                pre_idx = idx 
                count = 0 
            elif count == 1: 
                idx = ls.index(max(ls))
                if pre_idx != idx: 
                    count = 0 
                pre_idx = idx
        return result 

if __name__ == "__main__": 
    a, b, c = 0, 8, 11 
    s = Solution()
    assert len(s.longestDiverseString(a, b, c)) == 19