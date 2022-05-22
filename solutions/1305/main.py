from typing import * 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def traverse(self, node): 
        if node is None: 
            return [] 
        return self.traverse(node.left) + [node.val] + self.traverse(node.right) 
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        list1 = self.traverse(root1) 
        list2 = self.traverse(root2) 
        result = []
        i, j = 0, 0 
        while i < len(list1) and j < len(list2): 
            if list1[i] < list2[j]: 
                result.append(list1[i])
                i += 1 
            else: 
                result.append(list2[j])
                j += 1
        while i < len(list1): 
            result.append(list1[i])
            i += 1
        while j < len(list2): 
            result.append(list2[j])
            j += 1
        return result 

if __name__ == "__main__": 
    s = Solution()

    # root1 = [2,1,4]
    # root2 = [1,0,3]
    # assert s.getAllElements(root1, root2) == [0,1,1,2,3,4] 