from typing import * 

# 同样的测试，测试用例可以过，提交不能过，输出是错的
# 错误出在children={}
class TreeNode:
    # 不能用children={}
    def __init__(self, val=None, children={}, is_end=False): 
        self.val = val 
        self.children = children
        self.is_end = is_end

class Solution:
    def insert(self, d): 
        n = len(d)
        i = 0 
        nodes = self.root.children 
        while i < n and nodes.get(d[i], -1) != -1: 
            nodes = nodes[d[i]].children
            i += 1 
        while i < n: 
            nodes[d[i]] = TreeNode(d[i])
            if i == n-1: 
                node = nodes[d[i]]
                node.is_end = True
            nodes = nodes[d[i]].children 
            i += 1 

    def isSubDir(self, d): 
        n = len(d)
        i = 0 
        nodes = self.root.children
        while i < n and nodes.get(d[i], -1) != -1: 
            nodes = nodes[d[i]].children
            node = nodes[d[i]]
            if i != n-1 and node.is_end:
                return True 
            i += 1 
        return False  

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        self.root = TreeNode()

        for f in folder: 
            dirs = f.split("/")[1:]
            self.insert(dirs)
        
        res = []
        for f in folder: 
            dirs = f.split("/")[1:]
            if self.isSubDir(dirs):
                continue 
            res.append(f)

        return res 


if __name__ == "__main__":
    s = Solution()

    folder = ["/a/b/c","/a/b/ca","/a/b/d"]
    assert s.removeSubfolders(folder) == ["/a/b/c","/a/b/ca","/a/b/d"]

    # folder = ["/a","/a/b/c","/a/b/d"]
    # assert s.removeSubfolders(folder) == ["/a"]

    # folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
    # assert s.removeSubfolders(folder) == ["/a","/c/d","/c/f"]