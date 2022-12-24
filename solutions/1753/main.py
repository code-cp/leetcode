class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        res = 0 
        stones = [a, b, c]

        while True: 
            if len([x for x in stones if x != 0]) < 2: 
                break 
            stones.sort()
            stones[1] -= 1 
            stones[2] -= 1 
            res += 1 

        return res 
            

if __name__ == "__main__": 
    s = Solution() 

    a = 2
    b = 4
    c = 6
    assert s.maximumScore(a, b, c)