class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        my_dict = {}
        max_dist = -1 
        for i, ch in enumerate(s): 
            if ch not in my_dict: 
                my_dict[ch] = [i, 0]
            else: 
                my_dict[ch][1] = i 
                dist = i - my_dict[ch][0] - 1 
                max_dist = max(dist, max_dist)
        return max_dist 
