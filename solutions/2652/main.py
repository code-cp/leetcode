class Solution:
    def sumOfMultiples(self, n: int) -> int:
        # ref https://leetcode.cn/problems/sum-multiples/solutions/2241283/o1-rong-chi-yuan-li-by-endlesscheng-yxc4/?envType=daily-question&envId=Invalid+Date
        def s(m: int) -> int: 
            # k(k+1)/2*m
            return (n//m)*(n//m+1)//2*m
        return s(3)+s(5)+s(7)-s(15)-s(21)-s(35)+s(105)