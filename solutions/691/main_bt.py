from typing import * 

from collections import defaultdict 
class Solution:
    def backtracking(self, stickers, target, state, num_stickers):
        def applySticker(s, t):  
            res = t
            state = 0
            # for c in t: 
            #     if c != "?": 
            #         t0 = c 
            #         break 
            # if t0 not in s: 
            #     return False, None, None 
            for c in s: 
                if c in res: 
                    i = res.find(c)
                    temp = list(res)
                    temp[i] = '?'
                    res = ''.join(temp)   
            for i in range(len(res)): 
                if res[i] == "?": 
                    state |= 1 << i
            return True, res, state

        # base case 
        if num_stickers >= self.min_num_stickers: 
            return  
        if state == (1 << len(target)) - 1:
            self.min_num_stickers = min(num_stickers, self.min_num_stickers) 
            return
        if num_stickers != 0 and num_stickers >= self.memo[state]: 
            return 
        self.memo[state] = num_stickers 

        for i in range(len(stickers)): 
            apply_flag, new_target, new_state = applySticker(stickers[i], target)
            if not apply_flag: 
                continue 
            self.backtracking(stickers, new_target, new_state, num_stickers + 1)


    def minStickers(self, stickers: List[str], target: str) -> int:
        def checkDom(s1, s2):
            s1_in_s2 = True 
            s2_in_s1 = True 
            for c in s1: 
                if s1.count(c) > s2.count(c):
                    s1_in_s2 = False 
            for c in s2: 
                if s1.count(c) < s2.count(c):
                    s2_in_s1 = False 
            if s1_in_s2:
                return [s2]
            if s2_in_s1:
                return [s1]
            return [s1, s2] 

        def keepTarget(target, stickers): 
            new_stickers = []
            for st in stickers: 
                keep = [] 
                for i in range(len(st)): 
                    if st[i] in target: 
                        keep.append(st[i]) 
                if len(keep): 
                    new_st = ''.join(keep)  
                    new_stickers.append(new_st) 
            return new_stickers

        stickers = keepTarget(target, stickers)
        keep = [] 
        for i in range(len(stickers)): 
            for j in range(i+1, len(stickers)): 
                keep += checkDom(stickers[i], stickers[j])
        stickers = keep  

        self.min_num_stickers = 16
        self.memo = defaultdict(lambda:16) 
        self.backtracking(stickers, target, 0, 0) 
        if self.min_num_stickers == 16: 
            return -1 
        else: 
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

    # test TLE 
    stickers = ["heart","seven","consider","just","less","back","an","four","cost","kill","skin","happen","depend","broad","caught","fast","fig","way","under","print","white","war","sent","locate","be","noise","door","get","burn","quite","eight","press","eye","wave","bread","wont","short","cow","plain","who","well","drive","fact","chief","store","night","operate","page","south","once"]
    target = "simpleexample"
    s.minStickers(stickers, target) 