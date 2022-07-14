from typing import * 

# TLE 

class TreeNode: 
    def __init__(self, ch): 
        self.ch = ch 
        self.is_end = False 
        self.children = {}
        self.index = -1 

class WordFilter:
    # Take "apple" as an example, we will 
    # insert add "apple{apple", "pple{apple", "ple{apple", "le{apple", "e{apple", "{apple" 
    # into the Trie Tree.
    def __init__(self, words: List[str]):
        self.root = TreeNode("")
        for w in words: 
            res = self.transform(w)
            for r in res: 
                node = self.root 
                for ch in r: 
                    if ch not in node.children: 
                        node.children[ch] = TreeNode(ch)
                    node = node.children[ch]
                node.is_end = True 
                # NOTE, need to find last index of duplicates 
                node.index = len(words)-1-words[::-1].index(w)

    @staticmethod
    def transform(word):
        res = []
        for i in range(len(word)):
            suf = word[i:] 
            new_w = suf + "{" + word 
            res.append(new_w)
        return res 

    def search(self, node, res):
        # base case 
        if node.is_end:
            res.append(node.index)
            return 
        for _, n in node.children.items():
            self.search(n, res)

    def f(self, pref: str, suff: str) -> int:
        new_w = suff + "{" + pref 
        node = self.root  
        valid = []
        for ch in new_w: 
            if ch not in node.children:
                return -1 
            node = node.children[ch]
        res = []
        self.search(node, res)
        return max(res)

if __name__ == "__main__": 
    words = ["apple"]
    pref, suff = "a", "e"
    obj = WordFilter(words)
    param_1 = obj.f(pref, suff)