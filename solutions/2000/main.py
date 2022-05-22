class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word_list = list(word)
        stack = []
        for w in word_list: 
            stack.append(w)
            if w == ch: 
                n = len(stack)
                for i in range(n): 
                    word_list[i] = stack.pop()
                return "".join(word_list) 
        return word 

if __name__ == "__main__": 
    word = "abcdefd"
    ch = "d"
    s = Solution()
    assert s.reversePrefix(word, ch) == "dcbaefd"

