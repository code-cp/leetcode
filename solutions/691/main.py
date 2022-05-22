from typing import * 

from collections import defaultdict 
class Solution:
    def backtracking(self, stickers, target, state, num_stickers, start_index):
        def applySticker(s, t, start_index):  
            res = t
            state = 0
            # prune 
            # ref https://leetcode.com/problems/stickers-to-spell-word/discuss/108318/C++JavaPython-DP-+-Memoization-with-optimization-29-ms-(C++)
            # explicitly require next sticker containing target[0], which significantly reduced the search space.
            if t[start_index] not in s: 
                return False, None, None, None
            for c in s: 
                if c in res: 
                    i = res.find(c)
                    temp = list(res)
                    temp[i] = '?'
                    res = ''.join(temp) 
            found_start = False   
            for i in range(len(res)): 
                if res[i] == "?": 
                    state |= 1 << i
                elif not found_start: 
                    start_index = i 
                    found_start = True 
            return True, res, state, start_index

        # base case 
        # prune
        if num_stickers >= self.min_num_stickers: 
            return  
        if state == (1 << len(target)) - 1:
            self.min_num_stickers = min(num_stickers, self.min_num_stickers) 
            return
        # prune
        if num_stickers != 0 and num_stickers >= self.memo[state]: 
            return 
        self.memo[state] = num_stickers 

        for i in range(len(stickers)): 
            apply_flag, new_target, new_state, new_start_index = applySticker(stickers[i], target, start_index)
            if not apply_flag: 
                continue 
            self.backtracking(stickers, new_target, new_state, num_stickers + 1, new_start_index)


    def minStickers(self, stickers: List[str], target: str) -> int:
        # prune
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

        # prune
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
        self.backtracking(stickers, target, 0, 0, 0) 
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

    # test TLE 
    stickers = ["heart","major","sail","art","family","soon","one","design","want","skin","corner","miss","cotton","where","stood","winter","clock","tube","since","charge","music","hill","lot","new","meant","repeat","corn","after","excite","insect","produce","trade","office","cool","grew","last","these","island","cry","tree","value","thought","i","nose","each","push","through","egg","order","fact"]
    target = "ideacost"
    s.minStickers(stickers, target) 