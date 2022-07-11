from typing import * 

class TreeNode: 
    def __init__(self, ch): 
        self.char = ch 
        self.children = {}
        self.is_end = False 

class MagicDictionary:

    def __init__(self):
        self.root = TreeNode("")

    def buildDict(self, dictionary: List[str]) -> None:
        for d in dictionary:
            node = self.root 
            for ch in d: 
                if ch not in node.children:
                    tr = TreeNode(ch)
                    node.children[ch] = tr 
                node = node.children[ch]
            node.is_end = True 

    def search(self, searchWord: str) -> bool:
        def dfs(node, word):
            for ch in word:
                if ch not in node.children:
                    return False 
                node = node.children[ch]
            return node.is_end 

        node = self.root
        # only two case, either ch in node.children or ch not in node.children
        for i, ch in enumerate(searchWord):
            # check if can skip node.children
            for _, n in node.children.items():
                if dfs(n, searchWord[i+1:]):
                    if ch != n.char:
                        return True   
            # if cannot skip, then ch must in node.children
            if ch not in node.children:
                return False 
            node = node.children[ch]
        return False 

if __name__ == "__main__": 
    m = MagicDictionary()

    dictionary = ["hello", "leetcode"]
    m.buildDict(dictionary)
    assert not m.search("hello")
    assert m.search("hhllo")
    assert not m.search("hell")
    assert not m.search("leetcoded")


     

