class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def calSum(num):
            # calculate left part 
            first = num-index
            if first > 0: 
                left = (first+num-1)*(index)/2
            else: 
                left = (1+num-1)*(num-1)/2
                left += index-(num-1)
            # calculate the right part 
            first = num-(n-1-index)
            if first > 0: 
                right = (first+num-1)*(n-1-index)/2
            else: 
                right = (1+num-1)*(num-1)/2
                right += n-1-index-(num-1)
            return left+num+right 

        l, r = 1, maxSum
        while l <= r: 
            mid = (r-l)//2+l
            total = calSum(mid)
            if total <= maxSum: 
                l = mid+1
            else: 
                r = mid-1 
        return l-1  

if __name__ == "__main__":
    s = Solution() 

    # nums = [5,6,7]
    assert s.maxValue(3, 2, 18) == 7
    # nums = [1,1,1,1,1,2,3,4]
    assert s.maxValue(8, 7, 14) == 4
    # nums = [2,3,2,1,1,1]
    assert s.maxValue(6, 1, 10) == 3
    # nums = [1,1,2,1]
    assert s.maxValue(4, 2, 6) == 2 