class Solution:
    def distMoney(self, money: int, children: int) -> int:
        money -= children 
        ans = min(money // 7, children) 
        reminder = money - 7 * ans  
        
        if children - ans == 1 and reminder == 3:
            ans -= 1 
        elif children - ans == 0 and reminder > 0: 
            ans -= 1 
       
        if ans < 0: 
            return -1 
        
        return ans 