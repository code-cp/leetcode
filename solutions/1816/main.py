class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split(" ")
        result = " ".join(words[:k])
        return result 

if __name__ == "__main__": 
    s = "Hello how are you Contestant"
    k = 4
    ans = "Hello how are you"
    sol = Solution()
    assert sol.truncateSentence(s, k) == ans
