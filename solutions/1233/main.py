from typing import * 

class TreeNode:
    def __init__(self, val=None, is_end=False): 
        self.val = val 
        self.children = {}
        self.is_end = is_end

class Solution:
    def insert(self, d): 
        is_sub = False 
        n = len(d)
        i = 0 
        nodes = self.root.children 
        while i < n and nodes.get(d[i], None) is not None: 
            node = nodes[d[i]]
            if node.is_end: 
                is_sub = True 
            nodes = node.children
            i += 1 
        while i < n: 
            node = TreeNode(d[i]) 
            nodes[d[i]] = node
            nodes = node.children 
            if i == n-1: 
                node.is_end = True 
            i += 1 
        return is_sub 

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        self.root = TreeNode(None, None)

        res = []
        for f in folder: 
            dirs = f.split("/")[1:]
            if self.insert(dirs):
                continue 
            res.append(f)
    
        return res 


if __name__ == "__main__":
    s = Solution()

    folder = ["/a/b/c","/a/b/ca","/a/b/d"]
    assert s.removeSubfolders(folder) == ["/a/b/c","/a/b/ca","/a/b/d"]

    folder = ["/a","/a/b/c","/a/b/d"]
    assert s.removeSubfolders(folder) == ["/a"]

    folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
    assert s.removeSubfolders(folder) == ["/a","/c/d","/c/f"]