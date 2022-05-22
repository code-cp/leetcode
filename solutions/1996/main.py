from typing import List 

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        result = 0
        properties.sort(reverse=True)
        max_def = 0 
        j = 0 
        for i in range(len(properties)): 
            while properties[j][0] > properties[i][0] and j < len(properties):  
                if max_def < properties[j][1]: 
                    max_def = properties[j][1]
                j += 1
            if max_def > properties[i][1]:
                result += 1 
        return result 

if __name__ == "__main__": 
    properties = [[7,9],[10,7],[6,9],[10,4],[7,5],[7,10]]
    s = Solution()
    assert s.numberOfWeakCharacters(properties) == 2 