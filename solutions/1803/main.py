from typing import * 

class TrieNode:
    def __init__(self): 
        self.next = [None]*2 
        self.count = 0 

class Solution:
    def countNumSmallerThan(self, root, num, thres):
        count = 0 
        node = root 
        for i in range(15, -1, -1): 
            c = (thres >> i) & 1 
            b = (num >> i) & 1 
            # a^b = c 
            a = c^b 

            if a == 1 and c == 1: 
                # go to 0, all lower than thres 
                if node.next[0]:
                    count += node.next[0].count 

                # go to 1, same with thres currently 
                # NOTE, if node.next[1] is None, need to break 
                # since we already counted node.next[0] branch
                # and there is no more node.next[1] branch 
                # NOTE, only need to break in node = node.next[x] branch
                # this is to avoid double counting 
                # no need to break in count += node.next[x].count
                if node.next[1]:
                    node = node.next[1]
                else:
                    break 
            elif a == 1 and c == 0: 
                if node.next[1]:
                    node = node.next[1]
                else:
                    break 
            elif a == 0 and c == 1: 
                # go to 1
                if node.next[1]:
                    count += node.next[1].count 

                # go to 0 
                # NOTE, if node.next[0] is None, need to break 
                if node.next[0]:
                    node = node.next[0]
                else:
                    break 
            else: 
                if node.next[0]:
                    node = node.next[0]
                else:
                    break 

        return count 

    def insert(self, root, n): 
        node = root 
        for i in range(15, -1, -1):     
            if ((n>>i) & 1) == 1: 
                if node.next[1] is None: 
                    node.next[1] = TrieNode()
                node = node.next[1]
                node.count += 1 
            else: 
                if node.next[0] is None: 
                    node.next[0] = TrieNode()
                node = node.next[0]
                node.count += 1

    def countPairsSmallerThan(self, nums, thres): 
        root = TrieNode()
        count = 0 
        for n in nums: 
            count += self.countNumSmallerThan(root, n, thres)
            self.insert(root, n)
        return count 

    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        cnt1 = self.countPairsSmallerThan(nums, high+1)
        cnt2 = self.countPairsSmallerThan(nums, low)
        res = cnt1 - cnt2 
        return res 

if __name__ == "__main__": 
    s = Solution() 

    nums = [9,8,4,2,1]
    low = 5
    high = 14
    assert s.countPairs(nums, low, high) == 8

    # nums = [1,4,2,7]
    # low = 2
    # high = 6
    # assert s.countPairs(nums, low, high) == 6 




# wrong version 
# class Solution:
#     def countPairs(self, nums: List[int], low: int, high: int) -> int:
#         class TrieNode:
#             def __init__(self): 
#                 self.next = [None]*2 
#                 self.count = 0 

#         def countNumSmallerThan(root, num, thres):
#             count = 0 
#             node = root 
#             for i in range(31, -1, -1): 
#                 c = (thres >> i) & 1 
#                 b = (num >> i) & 1 
#                 # a^b = c 
#                 a = b ^ c 

#                 if a == 1 and c == 1: 
#                     # go to 0, all lower than thres 
#                     if node.next[0]:
#                         count += node.next[0].count 
#                     # go to 1, same with thres currently 
#                     if node.next[1]:
#                         node = node.next[1]
#                     if node.next[0] == None and node.next[1] == None:
#                         break 
#                 elif a == 0 and c == 1: 
#                     # go to 0 
#                     if node.next[0]:
#                         node = node.next[0]
#                     # go to 1 
#                     if node.next[1]:
#                         count += node.next[1].count 
#                     if node.next[0] == None and node.next[1] == None:
#                         break 
#                 elif a == 1 and c == 0: 
#                     if node.next[1]:
#                         node = node.next[1]
#                     else:
#                         break 
#                 else: 
#                     if node.next[0]:
#                         node = node.next[0]
#                     else:
#                         break 

#             return count 

#         def insert(root, n): 
#             node = root 
#             for i in range(31, -1, -1):     
#                 if (n>>i) & 1 == 1: 
#                     if node.next[1] is None: 
#                         node.next[1] = TrieNode()
#                     node = node.next[1]
#                     node.count += 1 
#                 else: 
#                     if node.next[0] is None: 
#                         node.next[0] = TrieNode()
#                     node = node.next[0]
#                     node.count += 1

#         def countPairsSmallerThan(thres): 
#             root = TrieNode()
#             count = 0 
#             for n in nums: 
#                 count += countNumSmallerThan(root, n, thres)
#                 insert(root, n)
#             return count 

#         cnt1 = countPairsSmallerThan(high+1)
#         cnt2 = countPairsSmallerThan(low)
#         res = cnt1 - cnt2 
#         return res 