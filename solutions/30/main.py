from typing import * 

from collections import defaultdict 
class Solution:        
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        words_dict = defaultdict(int)
        for w in words: 
            words_dict[w] += 1 
        word_len = len(words[0])
        total_len = word_len * len(words)


        res = []
        def dfs(s, c): 
            # base case
            if sum([y for x, y in words_dict.items()]) == 0:
                res.append(c-total_len)
                return 
            cur_word = s[c:c+word_len]
            for x, y in words_dict.items(): 
                if y == 0: 
                    continue 
                if x == cur_word:
                    words_dict[x] -= 1 
                    dfs(s, c+word_len)
                    words_dict[x] += 1 
        
        for cur_p in range(0, len(s)-total_len+1): 
            dfs(s, cur_p) 

        return res 

if __name__ == "__main__": 
    sol = Solution()

    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","good"]
    assert sol.findSubstring(s, words) == [8]

    s = "barfoothefoobarman"
    words = ["foo","bar"]
    assert sol.findSubstring(s, words) == [0,9]