from typing import List 

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        tokens = path.split("/")
        for t in tokens:
            if t == "" or t == ".":
                continue
            if t == "..":
                if len(stack) > 0:
                    stack.pop()
                continue
            stack.append(t)
        if len(stack) == 0:
            return "/"
        result = ""
        while len(stack) > 0:
            result = "/" + stack[-1] + result
            stack.pop()
        return result

if __name__ == "__main__": 
    path = "/a/../../b/../c//.//"
    s = Solution()
    assert s.simplifyPath(path) == "/c"
