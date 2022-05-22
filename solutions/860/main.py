from typing import List 

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        numFive = 0
        numTen = 0
        for i in range(len(bills)):
            if bills[i] == 5:
                numFive += 1
            elif bills[i] == 10:
                numFive -= 1
                numTen += 1
                if numFive < 0:
                    return False
            else:
                if numTen > 0:
                    numTen -= 1
                    numFive -= 1
                    if numTen < 0 or numFive < 0:
                        return False
                else:
                    numFive -= 3
                    if numFive < 0:
                        return False
        return True

if __name__ == "__main__":
    mySol = Solution()
    bills = [5,5,5,10,20]
    assert mySol.lemonadeChange(bills)
