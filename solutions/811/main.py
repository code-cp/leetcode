from typing import * 

from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = []
        my_domain = defaultdict(int)
        for cdomain in cpdomains: 
            s = cdomain.split(" ")
            count = int(s[0])
            domain = s[1]
            ds = domain.split(".")
            for i in range(len(ds)-1, -1, -1): 
                d = ".".join(ds[i:])
                my_domain[d] += count
        for k, v in my_domain.items():
            s = str(v) + " " + k
            res.append(s)
        return res 

if __name__ == "__main__": 
    s = Solution()

    cpdomains = ["9001 discuss.leetcode.com"]
    assert s.subdomainVisits(cpdomains) 