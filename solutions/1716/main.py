class Solution:
    def totalMoney(self, n: int) -> int:
        result = 0
        last_monday = 0
        last_deposit = 0
        cur_day = 0

        while cur_day != n: 
            cur_day += 1
            if cur_day % 7 != 1:
                deposit = last_deposit + 1 
            else: 
                deposit = last_monday + 1 
                last_monday = deposit
            result += deposit
            last_deposit = deposit 
        return result 

if __name__ == "__main__": 
    n = 20
    s = Solution()
    assert s.totalMoney(n) == 96
