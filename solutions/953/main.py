from typing import * 

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        pre = words[0]
        for i in range(1, len(words)): 
            cur = words[i]
            for j in range(len(pre)):
                if j < len(cur):
                    if order.find(pre[j]) > order.find(cur[j]):
                        return False 
                    elif order.find(pre[j]) == order.find(cur[j]): 
                        continue 
                    else: 
                        break 
                else: 
                    return False 
            pre = cur 
        return True 

if __name__ == "__main__": 
    s = Solution() 

    words = ["hello","leetcode"] 
    order = "hlabcdefgijkmnopqrstuvwxyz" 
    assert s.isAlienSorted(words, order) 

    words = ["word","world","row"]
    order = "worldabcefghijkmnpqstuvxyz"
    assert not s.isAlienSorted(words, order)