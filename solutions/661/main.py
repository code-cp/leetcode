from typing import * 

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        total = [[0] * (n+1) for _ in range(m+1)]
        # NOTE, prefix index should add 1 
        for i in range(1, m+1): 
            for j in range(1, n+1): 
                total[i][j] = total[i-1][j] + total[i][j-1] - total[i-1][j-1] + img[i-1][j-1]
        result = [[0] * n for _ in range(m)]
        kernel_size = 3 
        for i in range(0, m): 
            for j in range(0, n): 
                a, b = max(0, i-kernel_size//2), max(0, j-kernel_size//2)
                c, d = min(m-1, i+kernel_size//2), min(n-1, j+kernel_size//2)
                num = (c-a+1) * (d-b+1)
                # this is the total sum of range in (a+1, b+1) to (c+1, d+1)
                avg = total[c+1][d+1] - total[a][d+1] - total[c+1][b] + total[a][b]
                result[i][j] = avg//num 
        return result 

if __name__ == "__main__": 
    s = Solution()

    img = [[100,200,100],[200,50,200],[100,200,100]]
    ans = [[137,141,137],[141,138,141],[137,141,137]]
    result = s.imageSmoother(img)
    assert result == ans 