from typing import * 

# https://leetcode.cn/problems/stream-of-characters/solutions/2187661/bu-chao-gang-de-pu-tong-zi-dian-shu-zuo-9ax46/
# 由于查询后缀比较麻烦，可以转化为查询前缀，即把words里的所有单词全部反转，并且把字符流的顺序也视为反转。

class TrieNode: 
    def __init__(self, val): 
        self.val = val 
        self.children = {}
        self.is_end = False 

class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TrieNode(None)
        for w in words:
            w = w[::-1]
            cur = self.root  
            for ch in w: 
                if ch not in cur.children: 
                    cur.children[ch] = TrieNode(ch)
                cur = cur.children[ch]
            cur.is_end = True
             
        self.s = []    

    def query(self, letter: str) -> bool: 
        self.s.append(letter)
        n = len(self.s)
        cur = self.root 
        for i in range(n-1, -1, -1): 
            ch = self.s[i]
            if ch not in cur.children: 
                return False 
            cur = cur.children[ch]
            if cur.is_end: 
                return True 
        return False 

