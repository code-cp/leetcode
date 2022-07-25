# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque 
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root 

    def insert(self, val: int) -> int:
        # level order traversal 
        que = deque()
        que.append(self.root)
        par_node = None 
        pre_nodes = [] 
        cur_nodes = []
        level = -1 
        while len(que) > 0: 
            l = len(que)
            pre_nodes = [i for i in cur_nodes]
            cur_nodes = []
            level += 1 
            for i in range(l): 
                node = que.popleft()
                cur_nodes.append(node)
                if i == 0:
                    left_most = node
                if node.left: 
                    par_node = node 
                    que.append(node.left)
                if node.right: 
                    par_node = node 
                    que.append(node.right)
        if par_node is None: 
            self.root.left = TreeNode(val)
            par_node = self.root
        elif par_node.left is not None and par_node.right is None: 
            par_node.right = TreeNode(val)
        elif len(cur_nodes) == 2 ** level:
            par_node = cur_nodes[0] 
            par_node.left = TreeNode(val)
        else: 
            for node in pre_nodes:
                if node.left is None: 
                    print(node.val)
                    node.left = TreeNode(val)
                    par_node = node
                    break 
        return par_node.val 

    def get_root(self) -> TreeNode:
        return self.root 
