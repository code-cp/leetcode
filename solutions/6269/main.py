from typing import * 
import math 
class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if words[startIndex] == target: 
            return 0 

        n = len(words)
        found = False 

        cnt1 = 0
        i = (startIndex + 1) % n
        while i != startIndex: 
            cnt1 += 1 
            if words[i] == target: 
                found = True 
                break 
            i = (i + 1) % n

        cnt2 = 0
        i = (startIndex - 1 + n) % n
        while i != startIndex: 
            cnt2 += 1 
            if words[i] == target: 
                found = True 
                break 
            i = (i - 1 + n) % n

        res = min(cnt1, cnt2)
        return res if found else -1 

if __name__ == "__main__": 
    s = Solution() 

    words = ["ixgfxcpcbc","noltxvwjfu","uxtsrnulju","noltxvwjfu","hsojlwnjew","mmppqxgzub","hesbexhwxo","ybjeptueck","hsojlwnjew","iuqgsokpbk"]
    target = "ybjeptueck"
    startIndex = 9
    assert s.closetTarget(words, target, startIndex) == 2 

    # words = ["a","b","leetcode"]
    # target = "leetcode"
    # startIndex = 0
    # assert s.closetTarget(words, target, startIndex) == 1 

    # words = ["i","eat","leetcode"]
    # target = "ate"
    # startIndex = 0
    # assert s.closetTarget(words, target, startIndex) == -1 

    # words = ["hello","i","am","leetcode","hello"]
    # target = "hello"
    # startIndex = 1
    # assert s.closetTarget(words, target, startIndex) == 1 