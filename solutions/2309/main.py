
class Solution:
    def greatestLetter(self, s: str) -> str:
        res = ""
        letters = {}
        for ch in s:  
            if letters.get(ch, -1) == -1: 
                letters[ch] = 0 
            letters[ch] += 1
            if ch.isupper(): 
                if letters.get(ch.lower(), -1) > 0:
                    res = ch if len(res) == 0 or ord(ch) > ord(res) else res 
            else: 
                if letters.get(ch.upper(), -1) > 0:
                    res = ch.upper() if len(res) == 0 or ord(ch.upper()) > ord(res) else res 
        return res

if __name__ == "__main__": 
    s = Solution() 

    assert s.greatestLetter("arRAzFif") == "R"
    # assert s.greatestLetter("lEeTcOdE") == "E"