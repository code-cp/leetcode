from typing import * 

class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        # dp[i] is max total height stacked from first i cuboids 
        # and select i-th cuboid as bottom one 
        n = len(cuboids)
        shapes = []

        for i in range(n):
            l, w, h = cuboids[i][0], cuboids[i][1], cuboids[i][2]
            shapes.append((l,w,h,i))
            shapes.append((l,h,w,i))
            shapes.append((w,h,l,i))
            shapes.append((w,l,h,i))
            shapes.append((h,w,l,i))
            shapes.append((h,l,w,i))

        shapes.sort()
        
        dp = [0] * (6*n)
        for i in range(6*n): 
            dp[i] = shapes[i][2]
            for j in range(i): 
                if shapes[j][0] <= shapes[i][0] and shapes[j][1] <= shapes[i][1] and shapes[j][2] <= shapes[i][2] and shapes[j][3] != shapes[i][3]:
                    dp[i] = max(dp[i], dp[j]+shapes[i][2])

        return max(dp)

if __name__ == "__main__": 
    s = Solution() 

    cuboids = [[50,45,20],[95,37,53],[45,23,12]]
    assert s.maxHeight(cuboids) == 190
