from collections import Counter 
class Solution:
    def equalFrequency(self, word: str) -> bool:
        cnt_w = Counter(word)
        freq_min = min(cnt_w.values())
        freq_max = max(cnt_w.values())
        cnt_f = Counter(cnt_w.values())
        if freq_max == freq_min: 
            if freq_min == 1:
                return True 
            if len(cnt_w.keys()) == 1: 
                return True 
        else: 
            if len(cnt_f.keys()) == 2:
                if freq_min == 1 and cnt_f[freq_min] == 1: 
                    return True 
                if freq_max == freq_min+1: 
                    return cnt_f[freq_max] == 1 
        return False 
    
if __name__ == "__main__": 
    s = Solution() 
    
    assert not s.equalFrequency("babbdd") 
    assert s.equalFrequency("cccd")  
    assert not s.equalFrequency("aazz")  
    assert s.equalFrequency("zz")  
    assert s.equalFrequency("abbcc") 