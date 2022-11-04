import math 
class Solution:
    def reachNumber(self, target: int) -> int:
        # due to symmetry 
        target = abs(target)
        x = count = 0 
        mySum = lambda n: n*(n+1)/2 

        def bsearch(target):
            # n*(n+1)/2 
            l, r = 1, int(math.sqrt(target*2))
            # find first number > target 
            while l <= r: 
                mid = (r-l)//2 + l 
                if mySum(mid) < target:
                    l = mid+1 
                else: 
                    r = mid-1 
            return l 

        count = bsearch(target)
        x = mySum(count)
        if x == target: 
            return count 
        elif (x - target) % 2 == 0: 
            # diff = n*(n+1)/2 - target < n 
            # diff is even -> n*(n+1)/2 - 2*i = target
            # i = diff/2 < n 
            return count 
        elif count % 2 == 0:
            # n+1+diff is even  
            return count+1 
        else: 
            # diff+1 is even
            # need to go back and then go forward 
            return count+2



if __name__ == "__main__": 
    s = Solution()

    target = 3 
    assert s.reachNumber(target) == 2 

    target = 1e9 
    assert s.reachNumber(target) == 44723

    # -1, 1, 4
    target = 4 
    assert s.reachNumber(target) == 3 

    target = 2 
    assert s.reachNumber(target) == 3 

    target = 3
    assert s.reachNumber(target) == 2 