from typing import * 

from collections import defaultdict
class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        ans = 0 
        cnt, frq = defaultdict(int), defaultdict(int)
        for i, n in enumerate(nums): 
            if cnt[n] > 0: 
                frq[cnt[n]] -= 1 
            cnt[n] += 1 
            frq[cnt[n]] += 1 

            # 如果所有的数频率相同，删除下一个出现的数
            # eg [1,1,2,2,3,3]
            total = frq[cnt[n]] * cnt[n]
            if total == i+1 and i != len(nums)-1: 
                ans = i+2
                continue 
            
            # 如果所有数频率不同
            # 除了当前频率的数，剩下的数只有两种可能
            # case a [1,1,2,2,3]
            # case b [1,1,2,2,3,3,3]
            rest = i+1 - total
            # 不同的频率只能出现一次，否则无法通过删除一个数达到要求
            if frq[rest] == 1: 
                if rest == cnt[n]+1 or rest == 1: 
                    ans = i+1 

        return ans 

if __name__ == "__main__": 
    s = Solution()

    nums = [2,2,1,1,5,3,3,5]
    assert s.maxEqualFreq(nums) == 7