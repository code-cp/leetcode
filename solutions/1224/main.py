from typing import * 

from collections import Counter
class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        freq, count = Counter(), Counter()
        ans = max_freq = 0 
        for i, num in enumerate(nums):
            if count[num]: 
                # 更新num的频率，因为num多出现了一次，旧的频率变了
                freq[count[num]] -= 1 
            count[num] += 1 
            freq[count[num]] += 1 

            max_freq = max(max_freq, count[num])

            # 最大出现次数 \textit{maxFreq} = 1maxFreq=1：那么所有数的出现次数都是一次，随意删除一个数既可符合要求。
            # 所有数的出现次数都是 \textit{maxFreq}maxFreq 或 \textit{maxFreq} - 1maxFreq−1，并且最大出现次数的数只有一个：删除一个最大出现次数的数，那么所有数的出现次数都是 \textit{maxFreq} - 1maxFreq−1。
            # 除开一个数，其他所有数的出现次数都是 \textit{maxFreq}maxFreq，并且该数的出现次数为 11：直接删除出现次数为 11 的数，那么所有数的出现次数都是 \textit{maxFreq}maxFreq。
            if max_freq == 1: 
                ans = max(ans, i+1)
            if freq[max_freq] * max_freq + freq[max_freq-1] * (max_freq - 1) == i+1 and freq[max_freq] == 1:
                ans = max(ans, i+1)
            if freq[max_freq] * max_freq + 1 == i+1 and freq[1] == 1: 
                ans = max(ans, i+1)

        return ans 
    