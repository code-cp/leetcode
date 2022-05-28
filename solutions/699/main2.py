class TreeNode:
    def __init__(self, l, r, v):
        self.left = l
        self.right = r 
        self.val = v

class ChthollyTree:
    def __init__(self, ):
        self.nodes = []

    def split(self, pos):
        n = len(self.nodes)
        left, right = 0, n-1
        while left <= right: 
            mid = (right - left)//2 + left 
            if self.nodes[mid].left < pos:
                left = mid + 1 
            elif self.nodes[mid].left > pos:
                right = mid - 1 
            else: 
                # no need to split if node.left == pos  
                return mid
        left -= 1 
        l, r, v = self.nodes[left].left, self.nodes[left].right, self.nodes[left].val 
        del self.nodes[left]
        tr = TreeNode(l, pos-1, v)  
        self.nodes.insert(left, tr)
        tr = TreeNode(pos, r, v)
        self.nodes.insert(left+1, tr)
        return left+1

    def assign(self, l, r, v): 
        if len(self.nodes) == 0: 
            tr = TreeNode(l, r, v) 
            self.nodes.append(tr)
            return 
        itr = self.split(r+1)
        itl = self.split(l) 
        del self.nodes[itl:itr]
        tr = TreeNode(l, r, v) 
        self.nodes.insert(itl, tr) 

class Solution(object):
    def fallingSquares(self, positions):
        ct = ChthollyTree() 
        results = [] 
        max_height = 0 
        ct.assign(1, 1e8, 0)
        for p in positions:
            itr = ct.split(p[0]+p[1])
            itl = ct.split(p[0])
            height = 0 
            for i in range(itl, itr+1): 
                height = max(ct.nodes[i].val + p[1], height)
                max_height = max(max_height, height) 
            ct.assign(p[0], p[0]+p[1]-1, height) 
            results.append(max_height)
        return results 

if __name__ == '__main__':
    s = Solution()

    positions = [[1,2],[2,3],[6,1]]
    assert s.fallingSquares(positions) == [2,5,5] 

    positions = [[100,100],[200,100]]
    assert s.fallingSquares(positions) == [100,100]