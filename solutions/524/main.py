from typing import List 

class Solution:
    @staticmethod
    def isSubseq(s, word):
        i, j = 0, 0
        while i < len(s) and j < len(word):
            if word[j] != s[i]:
                i += 1
            else:
                # avoid using same char
                i += 1
                j += 1
            if j == len(word):
                return True
        return False
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        # primary sorting key: length
        # secondary sorting key: lexicographically
        dictionary.sort(key=lambda x: (-len(x), x))
        for d in dictionary:
            if self.isSubseq(s, d):
                return d
        return ""

if __name__ == "__main__": 
    s = "abpcplea"
    dictionary = ["ale","apple","monkey","plea"]
    sol = Solution()
    assert sol.findLongestWord(s, dictionary) == "apple"
