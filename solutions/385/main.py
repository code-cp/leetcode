# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """
       pass 

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """
       pass

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """
       pass 

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """
       pass

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """
       pass

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """
       pass

from collections import deque 
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        stack = deque()
        num = ""
        for c in s:
            if c == '[':
                stack.append(NestedInteger())
            elif c in [',', ']']:
                if len(num) > 0: 
                    # NOTE, int() in python handles negative numbers 
                    stack[-1].add(NestedInteger(int(num)))
                    num = ""
                if c == ']' and len(stack) > 1: 
                    stack[-2].add(stack.pop())
            else: 
                # c is 0-9 or - 
                num += c 
        return stack[0] if len(stack) > 0 else NestedInteger(int(num)) 

# if __name__ == "__main__": 
#     s = Solution()
#     result = s.deserialize("[123,[456,[789]]]")
#     assert result == [123,[456,[789]]]