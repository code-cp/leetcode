from typing import List 

class Solution:
    def bitCount(self, num):
        count = 0
        while num:
            num = num & (num - 1)
            count += 1
        return count
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr = sorted(arr, key=lambda num: (self.bitCount(num), num))
        return arr

if __name__ == "__main__":
    arr = [0,1,2,3,4,5,6,7,8]
    s = Solution()
    print(s.sortByBits(arr))
