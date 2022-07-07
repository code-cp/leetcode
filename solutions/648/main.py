from typing import * 

class TreeNode:
    def __init__(self, val):
        self.ch = val
        self.children = {}
        self.is_end = False 

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = TreeNode("")
        for d in dictionary:
            node = root 
            for ch in d: 
                if ch not in node.children:
                    node.children[ch] = TreeNode(ch)
                node = node.children[ch]
            node.is_end = True 
        result = ""
        for s in sentence.split(" "):
            node = root 
            res = ""
            for ch in s:
                res += ch  
                if ch in node.children:
                    node = node.children[ch]
                    if node.is_end:
                        break 
                else: 
                    res = s 
                    break 
            result += res 
            result += " "
        return result.rstrip()

if __name__ == "__main__": 
    s = Solution() 

    # dictionary = ["cat","bat","rat"]
    # sentence = "the cattle was rattled by the battery"
    # assert s.replaceWords(dictionary, sentence) == "the cat was rat by the bat"

    dictionary = ["a", "aa", "aaa", "aaaa"]
    sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
    assert s.replaceWords(dictionary, sentence) == "a a a a a a a a bbb baba a"