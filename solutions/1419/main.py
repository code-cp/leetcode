class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        # //每一只青蛙可以处于5种状态，即c,r,o,a,k(不鸣叫和鸣叫结束都处于k)
        # //每个字符视为状态，由前一个字符转移而来，例如，遇到o，则需要将r-1，o+1
        # //无法转移时，如果当前字符为c，则可以增加一只青蛙，否则失败
        # //最终所有青蛙都要回到不鸣叫的状态，否则失败
        
        # 特斯拉公开笔试题目。
        
        sound = {
            'c':0,
            'r':1,
            'o':2,
            'a':3,
            'k':4, 
        }
        frogs = [0]*len(sound)
        ans = 0 
        
        for ch in croakOfFrogs: 
            if ch == "c":  
                if frogs[-1] > 0: 
                    # there are frogs at status k
                    frogs[0] += 1 
                    frogs[-1] -= 1 
                else: 
                    # there are no frogs at status k 
                    ans += 1 
                    frogs[0] += 1 
            else: 
                frogs[sound[ch]] += 1 
                if frogs[sound[ch]-1] > 0: 
                   frogs[sound[ch]-1] -= 1
                else: 
                    return -1 
                
        return ans if frogs[-1] == ans else -1 