class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        result = 0
        while target != 1: 
            if target % 2 == 1: 
                target -= 1 
                result += 1 
            else: 
                if maxDoubles > 0: 
                    maxDoubles -= 1 
                    result += 1 
                else: 
                    result += target / 2
                target /= 2
        return int(result) 

if __name__ == "__main__":
    target = 5
    maxDoubles = 0
    s = Solution()
    assert s.minMoves(target, maxDoubles) == 4
