from collections import defaultdict 
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_dict = defaultdict(int)
        for i, ch in enumerate(order): 
            order_dict[ch] = i + 1 
        return "".join(sorted(s, key=lambda ch: order_dict[ch]))
