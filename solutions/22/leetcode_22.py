class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        self.backtrack(ret, "", 0, 0, n)
        return ret 
    
    def backtrack(self, ret, cur_str, left_num, right_num, n):
        
        # base case 
        if (len(cur_str) == 2 * n):
            ret.append(cur_str)
            return ret 
        
        if (left_num < n):
            self.backtrack(ret, cur_str + "(", left_num + 1, right_num, n)
            
        if (right_num < left_num):
            self.backtrack(ret, cur_str + ")", left_num, right_num + 1, n)

if __name__ == "__main__":
    
    s = Solution()
    print(s.generateParenthesis(3))