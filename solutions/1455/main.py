class TreeNode:
    def __init__(self, val):
        self.val = val 
        self.children = {}

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(" ")
        root = TreeNode("")
        for i, w in enumerate(words):
            node = root 
            for ch in w: 
                if ch not in node.children:
                    node.children[ch] = (TreeNode(ch), i)
                node, _ = node.children[ch]
        node = root 
        for ch in searchWord:
            if ch in node.children:
                node, i = node.children[ch]
            else:
                return -1
        return i+1

if __name__ == "__main__": 
    s = Solution()

    sentence = "dumb dream duck duck i"
    searchWord = "drea"
    assert s.isPrefixOfWord(sentence, searchWord) == 2

    # sentence = "i love eating burger"
    # searchWord = "burg"
    # assert s.isPrefixOfWord(sentence, searchWord) == 4