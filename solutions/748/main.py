from typing import List 

class Solution:
    @staticmethod
    def str2tokens(s):
        result = [0]*26
        for c in s:
            if c == ' ':
                continue
            if ord(c) >= ord('0') and ord(c) <= ord('9'):
                continue
            result[ord(c.lower())-ord('a')] += 1
        return result
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        result = "x" * 20
        lpRes = self.str2tokens(licensePlate)
        for w in words:
            wRes = self.str2tokens(w)
            diff = [x - y for x, y in zip(lpRes, wRes)]
            pos = [x for x in diff if x > 0]
            if len(pos) > 0:
                continue
            else:
                if len(w) < len(result):
                    result = w
        return result

if __name__ == "__main__": 
    licensePlate = "1s3 PSt"
    words = ["step","steps","stripe","stepple"]
    s = Solution()
    assert s.shortestCompletingWord(licensePlate, words) == "steps"
