from typing import * 

# TLE 
class Solution:
    def backtracking(self, stickers, target, state, num_stickers):
        def applySticker(s, t): 
            apply_flag = False 
            res = [i for i in t]
            state = 0
            for i in range(26): 
                if s[i] > 0 and res[i] > 0:
                    res[i] = max(0, res[i] - s[i]) 
                    apply_flag = True 
                if res[i] == 0: 
                    state |= 1 << i 
            return apply_flag, res, state

        # base case 
        if num_stickers >= self.min_num_stickers: 
            return  
        if state == (1 << 26) - 1:
            self.min_num_stickers = min(num_stickers, self.min_num_stickers) 
            return

        for i in range(len(stickers)): 
            apply_flag, new_target, new_state = applySticker(stickers[i], target)
            if not apply_flag: 
                continue 
            self.backtracking(stickers, new_target, new_state, num_stickers + 1)


    def minStickers(self, stickers: List[str], target: str) -> int:
        def strToList(s): 
            res = [0] * 26  
            for c in s: 
                res[ord(c) - ord('a')] += 1 
            return res
        def checkDom(s1, s2): 
            for i in range(26): 
                if s1[i] > s2[i]:
                    return False 
            return True 
        stickers = [strToList(s) for s in stickers]
        to_rm = []
        for i in range(len(stickers)): 
            for j in range(i+1, len(stickers)): 
                if checkDom(stickers[i], stickers[j]):
                    to_rm.append(stickers[i])
        stickers = [st for st in stickers if st not in to_rm] 
        target = strToList(target) 
        self.min_num_stickers = float("inf") 
        self.backtracking(stickers, target, 0, 0) 
        if self.min_num_stickers == float("inf"): 
            return -1 
        else: 
            print(self.min_num_stickers)
            return self.min_num_stickers 


if __name__ == "__main__": 
    s = Solution() 
    
    stickers = ["with","example","science"]
    target = "thehat"
    assert s.minStickers(stickers, target) == 3 

    stickers = ["notice","possible"]
    target = "basicbasic"
    assert s.minStickers(stickers, target) == -1 

    stickers = ["these","guess","about","garden","him"]
    target = "atomher"
    assert s.minStickers(stickers, target) == 3 

    # test TLE 
    stickers = ["heavy","claim","seven","set","had","it","dead","jump","design","question","sugar","dress","any","special","ground","huge","use","busy","prove","there","lone","window","trip","also","hot","choose","tie","several","be","that","corn","after","excite","insect","cat","cook","glad","like","wont","gray","especially","level","when","cover","ocean","try","clean","property","root","wing"]
    target = "travelbell"
    assert s.minStickers(stickers, target) == 4  