from typing import * 

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ['a', 'e', 'i', 'o', 'u']
        n = len(words)
        prefix = [0]*(n+1) 
        for i, w in enumerate(words):
            prefix[i+1] = prefix[i] 
            if w[0] in vowels and w[-1] in vowels:
                prefix[i+1] += 1  
                
        ans = [0]*len(queries)
        for i, q in enumerate(queries):
            ans[i] = prefix[q[1]+1] - prefix[q[0]]
            
        return ans 
    
if __name__ == "__main__": 
    s = Solution() 
    
    words = ["aba","bcb","ece","aa","e"]
    queries = [[0,2],[1,4],[1,1]]
    assert s.vowelStrings(words, queries) == [2,3,0]
            
             
        