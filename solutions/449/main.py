from typing import * 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def traverse(node, res): 
            if node == None: 
                return 
            traverse(node.left, res) 
            traverse(node.right, res)
            res.append(node.val) 
        res = [] 
        traverse(root, res) 
        return " ".join(map(str, res)) 

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        def construct(arr: List[int], lower: int, upper: int) -> TreeNode: 
            if arr == [] or arr[-1] < lower or arr[-1] > upper: 
                return None 
            val = arr.pop()
            root = TreeNode(val) 
            # pop is LIFO 
            root.right = construct(arr, val, upper) 
            root.left = construct(arr, lower, val) 
            return root 
        arr = list(map(int, data.split()))
        return construct(arr, -float("inf"), float("inf"))
        

if __name__ == "__main__": 
    root = TreeNode(2)
    node1 = TreeNode(1)
    node3 = TreeNode(3)
    root.left = node1 
    root.right = node3 
    
    ser = Codec()
    deser = Codec()

    tree = ser.serialize(root)
    ans = deser.deserialize(tree)
    