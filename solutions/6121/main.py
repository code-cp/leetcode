from typing import * 

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        sortList = lambda l: sorted(range(len(l)), key=lambda k: l[k])
        ans = []
        trim_results = {}
        for q in queries: 
            if q[1] in trim_results:
                temp = trim_results[q[1]]
                ans.append(temp[q[0]-1])
                continue 
            new_nums = []
            for n in nums: 
                n = n[-q[1]:]
                new_nums.append(n)
            sort_num = sortList(new_nums)
            trim_results[q[1]] = sort_num 
            ans.append(sort_num[q[0]-1])
        return ans 

if __name__ == "__main__": 
    s = Solution()

    nums = ["102","473","251","814"]
    queries = [[1,1],[2,3],[4,2],[1,2]]
    assert s.smallestTrimmedNumbers(nums, queries) == [2,2,1,0]

    nums = ["24","37","96","04"]
    queries = [[2,1],[2,2]]
    assert s.smallestTrimmedNumbers(nums, queries) == [3,0]
