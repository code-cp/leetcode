from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_dict = defaultdict(int)
        balloon = "balloon"
        for t in text: 
            if t in balloon: 
                balloon_dict[t] += 1 
        result = float("inf")
        for i in range(len(balloon)):
            factor = 1 
            if i == 2 or i == 4:
                factor = 2 
            result = min(balloon_dict[balloon[i]] // factor, result)
        return result

if __name__ == "__main__": 
    text = "loonbalxballpoon"
    s = Solution()
    assert s.maxNumberOfBalloons(text) == 2