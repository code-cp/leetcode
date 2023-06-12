from typing import * 
from collections import deque 
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def findM(w): 
            cnt = Counter(w)
            km = "z"
            for k, v in cnt.items():
                if ord(k) < ord(km):
                    km = k 
            return cnt[km]
        
        ans = []
        cnt = []
        inf = float("inf")
        for w in words: 
            cnt.append(findM(w))
        for q in queries: 
            m = findM(q)
            ans.append(len([x for x in cnt if x > m]))
            
        return ans 
    
if __name__ == "__main__": 
    s = Solution() 
    
    queries = ["bbb","cc"]
    words = ["a","aa","aaa","aaaa"]
    assert s.numSmallerByFrequency(queries, words) == [1,2]
             
                    
        
            