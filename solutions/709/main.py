class Solution:
    def toLowerCase(self, s: str) -> str:
        result = []
        for c in s: 
            result.append(c.lower())
        return "".join(result)

if __name__ == "__main__": 
    s = "Hello"
    sol = Solution()
    ans = "hello"
    assert sol.toLowerCase(s) == ans
