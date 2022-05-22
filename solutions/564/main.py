from typing import * 

# ref https://leetcode.com/problems/find-the-closest-palindrome/discuss/102391/Python-Simple-with-Explanation
# https://leetcode.com/problems/find-the-closest-palindrome/discuss/102391/Python-Simple-with-Explanation/105839
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        l = len(n)
        candidates = set((str(10 ** l + 1), str(10 ** (l-1) - 1)))
        prefix = int(n[:(l+1)//2])
        for i in map(str, (prefix-1, prefix, prefix+1)):
            # two possibilities, eg: '11' or '1' 
            can = [i, i[:-1]]
            # if l is even, choose the first one, if l is odd, choose the second one 
            can = can[l & 1]
            # reverse 
            can = can[::-1]
            # add the prefix 
            can = i + can 
            candidates.add(can)
        # do not count n itself 
        candidates.discard(n)
        # first compare abs(int(x)-int(n)), then compare int(x)
        return min(candidates, key=lambda x: (abs(int(x)-int(n)), int(x)))

if __name__ == "__main__": 
    s = Solution()

    n = "123"
    result = s.nearestPalindromic(n)
    assert result == "121"