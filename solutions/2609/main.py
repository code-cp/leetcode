class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        n = len(s)
        prefix_zero = [0]*(n+1)
        prefix_one = [0]*(n+1) 
        
        ans = 0 
        
        for i in range(n): 
            prefix_zero[i+1] = prefix_zero[i] + (1 if s[i] == '0' else 0)
            prefix_one[i+1] = prefix_one[i] + (1 if s[i] == '1' else 0)
            
        for i in range(n): 
            for j in range(i+1, n): 
                sub = s[i:j+1]
                num1 = prefix_one[j+1]-prefix_one[i]
                num0 = prefix_zero[j+1]-prefix_zero[i]
                # check 0, 1 numbers 
                if num1!=num0:
                    continue 
                # check power of 2 
                if len(str(int(sub))) != num1: 
                    continue 

                ans = max(ans, j-i+1) 
                
        return ans 

if __name__ == "__main__": 
    s = Solution()
    
    assert s.findTheLongestBalancedSubstring("01000111") == 6 
    # assert s.findTheLongestBalancedSubstring("0011") == 4 