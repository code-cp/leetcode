from typing import * 

# ref https://stackoverflow.com/a/5389547/8519188
def grouped(iterable, n):
    "s -> (s0,s1,s2,...sn-1), (sn,sn+1,sn+2,...s2n-1), (s2n,s2n+1,s2n+2,...s3n-1), ..."
    return zip(*[iter(iterable)]*n)

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = [[] for _ in range(max(groupSizes)+1)]
        for i, gs in enumerate(groupSizes): 
            groups[gs].append(i)
        res = []
        for i, gp in enumerate(groups):
            for ps in grouped(gp, i):
                res.append(list(ps))
        return res 

if __name__ == "__main__": 
    s = Solution()

    groupSizes = [3,3,3,3,3,1,3]
    assert s.groupThePeople(groupSizes) == [[5],[0,1,2],[3,4,6]]
