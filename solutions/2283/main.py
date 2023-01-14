from collections import Counter 
class Solution:
    def digitCount(self, num: str) -> bool:
        cnt = Counter(num)
        for i, n in enumerate(num): 
            if cnt[str(i)] != int(n): 
                return False 
        return True  

if __name__ == "__main__": 
    s = Solution() 

    assert s.digitCount("1210")