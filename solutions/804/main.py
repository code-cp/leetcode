from typing import * 

# ref https://leetcode-cn.com/problems/unique-morse-code-words/solution/by-zhug-4-e1wt/

class Trie(): 
    def __init__(self, left=None, right=None): 
        self.is_end = False 
        self.left = left 
        self.right = right 
        self.word_count = 0 
    
    def insert(self, word): 
        node = self 
        for c in word: 
            if c == ".": 
                if not node.left: 
                    node.left = Trie()
                node = node.left 
            elif c == "-":
                if not node.right: 
                    node.right = Trie() 
                node = node.right 
        if not node.is_end: 
            node.is_end = True 
            self.word_count += 1 
            
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        T = Trie()
        for word in words:
            T.insert(''.join([codes[ord(c) - ord('a')] for c in word]))
        return T.word_count 

if __name__ == "__main__": 
    s = Solution()
    result = s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
    assert result == 2 