from typing import List 

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # record the rightmost place for each char
        hash = [0] * 26
        for i in range(len(s)):
            hash[ord(s[i]) - ord('a')] = i
        result = []
        left = 0
        right = 0
        for i in range(len(s)):
            right = max(right, hash[ord(s[i]) - ord('a')])
            if right == i:
                result.append(right - left + 1)
                left = right + 1
        return result

if __name__ == "__main__":
    s = "ababcbacadefegdehijhklij"
    mySol = Solution()
    print(mySol.partitionLabels(s))
