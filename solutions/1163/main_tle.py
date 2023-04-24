# The code works by using two pointers i and j to keep track of the current candidates for the last substring in lexicographical order. 
# 
# The pointer i points to the start of the current best substring, and the pointer j points to the start of another substring that is potentially larger than the current best. The offset k is used to compare the characters at i + k and j + k. 
# 
# If they are equal, we increase k and continue to compare the next characters. If the character at i + k is larger, we know that the substring starting from i is still larger than the substring starting from j, so we move j to j + k + 1 and reset k. 
# 
# If the character at j + k is larger, we know that the substring starting from j is larger than the substring starting from i, so we move i to j and move j to i + 1 and reset k. This way, we can find the largest substring in linear time by scanning the string only once.

# TLE 
# 
# s =
#"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

class Solution:
    def lastSubstring(self, s: str) -> str:
        # initialize two pointers i and j
        i = 0
        j = 1
        # initialize an offset k
        k = 0
        # loop until j reaches the end of the string
        while j + k < len(s):
            # compare the characters at i + k and j + k
            if s[i + k] == s[j + k]:
                # if they are equal, increase the offset and continue
                k += 1
            elif s[i + k] > s[j + k]:
                # if the character at i + k is larger, move j to j + k + 1 and reset k
                # NOTE, move j to j+k+1 not j+1, since we already compared [j+1,j+k]
                j = j + k + 1
                k = 0
            else:
                # if the character at j + k is larger, move i to j and move j to i + 1 and reset k
                i = j
                j = i + 1
                k = 0
        # return the substring starting from i
        return s[i:]
    
if __name__ == "__main__": 
    s = Solution() 
    
    # assert s.lastSubstring("abab") == "bab"
    assert s.lastSubstring("leetcode") == "tcode"