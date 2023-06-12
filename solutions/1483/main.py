from typing import * 

import math 
inf = float("inf")

# Binary Lifting 的本质其实是 dp。dp[node][j] 存储的是 node 节点距离为 2^j 的祖先是谁。

# 根据定义，dp[node][0] 就是 parent[node]，即 node 的距离为 1 的祖先是 parent[node]。

# 状态转移是： dp[node][j] = dp[dp[node][j - 1]][j - 1]。

# 意思是：要想找到 node 的距离 2^j 的祖先，先找到 node 的距离 2^(j - 1) 的祖先，然后，再找这个祖先的距离 2^(j - 1) 的祖先。两步得到 node 的距离为 2^j 的祖先。

# 作者：liuyubobobo
# 链接：https://leetcode.cn/problems/kth-ancestor-of-a-tree-node/solutions/1/li-kou-zai-zhu-jian-ba-acm-mo-ban-ti-ban-shang-lai/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.max_level = 32 - int(math.log(n, 2))
        # column: node index, row: level index 
        self.dp = [[0]*n for _ in range(self.max_level)] 
        self.dp[0] = parent
        for i in range(1, self.max_level): 
            for j in range(n): 
                if self.dp[i-1][j] == -1:
                    # if 2^i-1 does not have ancestor, then 2^i does not have ancestor  
                    self.dp[i][j] = -1 
                else: 
                    # 2^i-1 + 2^i-1 = 2^i 
                    self.dp[i][j] = self.dp[i-1][self.dp[i-1][j]]

    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(self.max_level): 
            if node == -1: 
                break 
            if k & (1 << i): 
                node = self.dp[i][node]
        return node 
    
if __name__ == "__main__": 
    n = 7 
    parent = [-1, 0, 0, 1, 1, 2, 2]
    s = TreeAncestor(n, parent)
    assert s.getKthAncestor(3, 1) == 1 