class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        result = -1 

        if len(a) != len(b): 
            result = max(len(a), len(b))
        else: 
            if a != b: 
                result = len(a)

        return result 

if __name__ == "__main__": 
    s = Solution()
    
    a = "aefawfawfawfaw"
    b = "aefawfeawfwafwaef"
    result = s.findLUSlength(a, b)
    assert result == 17 

    a = "abc"
    b = "bca"
    result = s.findLUSlength(a, b)
    assert result == 3