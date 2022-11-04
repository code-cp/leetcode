
# cannot do this in leetcode 
# max recursion limit exceeded 
import sys
sys.setrecursionlimit(int(5e4))

class Solution:
    def reachNumber(self, target: int) -> int:
        # due to symmetry 
        target = abs(target)
        x = count = 0 

        def dfs(x, target, count): 
            # base case 
            if x > target: 
                return float("inf") 
            if x == target: 
                return count 

            # go back and then go forward 
            # no need to go back twice, eg -i-i-1 = -2i-1
            # -2i-1+i+1 = -i, -i+i+2 = 2 
            # this is equivalent to -i-1, i, -i-1, i+2 
            count1 = dfs(x+1, target, count+2)
            # go forward 
            count2 = dfs(x+count+1, target, count+1)

            return min(count1, count2)

        count = dfs(x, target, count)
        return count 

if __name__ == "__main__": 
    s = Solution()

    target = 1e9 
    assert s.reachNumber(target) == 44723

    # -1, 1, 4
    target = 4 
    assert s.reachNumber(target) == 3 

    target = 2 
    assert s.reachNumber(target) == 3 

    target = 3
    assert s.reachNumber(target) == 2 