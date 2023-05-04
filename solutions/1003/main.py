from collections import deque 
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0: 
            return True 
        stack = deque()
        for i in range(len(s)):
            stack.append(s[i])
            if s[i] == "c": 
                while len(stack) >= 3 and stack[-1] == "c" and stack[-2] == "b" and stack[-3] == "a": 
                    stack.pop()
                    stack.pop()
                    stack.pop()
        return len(stack) == 0
    
if __name__ == "__main__": 
    s = Solution()
    assert s.isValid("aabcbc")
    assert not s.isValid("abccba")
    assert not s.isValid("bac")
    assert not s.isValid("aabbcc")
            