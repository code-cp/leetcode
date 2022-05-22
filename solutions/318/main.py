from typing import List 

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        maxProduct = 0
        wordsInt = []
        for w in words:
            result = 0
            for c in w:
                result |= 1 << ord(c) - ord('a')
            wordsInt.append(result)
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if wordsInt[i] & wordsInt[j]:
                    continue
                else:
                    product = len(words[i]) * len(words[j])
                    if product > maxProduct:
                        maxProduct = product
        return maxProduct

if __name__ == "__main__": 
    words = ["abcw","baz","foo","bar","xtfn","abcdef"]
    s = Solution()
    assert s.maxProduct(words) == 16
