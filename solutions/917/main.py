class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i, j = 0, len(s)-1 
        s_list = list(s)
        while i < j: 
            while i < len(s) and (ord(s_list[i].lower()) < ord('a') or ord(s_list[i].lower()) > ord('z')): 
                i += 1 
            while j > -1 and (ord(s_list[j].lower()) < ord('a') or ord(s_list[j].lower()) > ord('z')): 
                j -= 1
            if i < j and i < len(s) and j > -1: 
                temp = s_list[i]
                s_list[i] = s_list[j]
                s_list[j] = temp 
                i += 1 
                j -= 1 
        return "".join(s_list) 

if __name__ == "__main__": 
    sol = Solution()
    s = "ab-cd"
    assert sol.reverseOnlyLetters(s) == "dc-ba"
    s = "7_28]"
    assert sol.reverseOnlyLetters(s) == "7_28]"
    s = "?6C40E"
    assert sol.reverseOnlyLetters(s) == "?6E40C"