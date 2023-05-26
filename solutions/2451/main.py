from typing import * 

class Solution:
    def oddString(self, words: List[str]) -> str:
        hashmap = {}
        all_diff = []
        for w in words: 
            diff = []
            for i, ch in enumerate(w): 
                if i == 0: 
                    continue 
                diff.append(ord(ch)-ord(w[i-1]))
            k = tuple(diff)
            all_diff.append(k)
            hashmap[k] = hashmap.get(k, 0)+1
        for k, v in hashmap.items(): 
            if v == 1: 
                idx = all_diff.index(k)
                return words[idx]
            
            
             
                
                