from typing import * 

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        # utility functions 
        def crossProduct(a, b): 
            return a[0] * b[1] - a[1] * b[0]
        def findNextTree(a, b, c): 
            return crossProduct([c[0] - a[0], c[1] - a[1]], [b[0] - a[0], b[1] - a[1]]) 
        
        n = len(trees)

        if n < 4: 
            return trees 

        leftMostTree = 0 
        for i, (x, _) in enumerate(trees): 
            if x < trees[leftMostTree][0]: 
                leftMostTree = i 
        
        ans = []
        addedTree = []

        curTree = leftMostTree 
        while True: 
            candTree = (curTree + 1) % n   
            # find most clockwise tree 
            for i in range(n): 
                if findNextTree(trees[curTree], trees[candTree], trees[i]) > 0: 
                    candTree = i 

            # add all the trees that are most clockwise tree
            for i in range(n): 
                if findNextTree(trees[curTree], trees[candTree], trees[i]) == 0: 
                    if i not in addedTree:
                        ans.append(trees[i]) 
                        addedTree.append(i)

            curTree = candTree 

            if curTree == leftMostTree: 
                break 

        return ans 

if __name__ == "__main__":
    s = Solution()

    points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
    result = s.outerTrees(points)
    ans = [[1,1],[2,0],[3,3],[2,4],[4,2]]
    assert len(result) == len(ans)