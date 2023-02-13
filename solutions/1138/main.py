from collections import deque 
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        board[-1] = "z????"

        map_alpa_to_pos = {}
        m, n = len(board), len(board[0])
        for i in range(m): 
            for j in range(n): 
                map_alpa_to_pos[board[i][j]] = (i, j)
        
        res = ""
        dirs = [(0,1,"R"),(0,-1,"L"),(1,0,"D"),(-1,0,"U")]
        cur = (0,0,"")
        visited = [[0]*n for _ in range(m)]
        for tar in target: 
            q = deque()
            q.append(cur)
            while len(q) > 0: 
                q_len = len(q)
                for _ in range(q_len): 
                    pos = q.popleft()
                    if tar == board[pos[0]][pos[1]]:
                        res += pos[2] 
                        res += "!"
                        q.clear()
                        visited = [[0]*n for _ in range(m)]
                        break 
                    for d in dirs:
                        new_pos = (pos[0]+d[0], pos[1]+d[1], pos[2]+d[2])
                        if new_pos[0] < m and new_pos[1] < n: 
                            if new_pos[0] >= 0 and new_pos[1] >= 0:
                                if board[new_pos[0]][new_pos[1]] != "?":
                                    if visited[new_pos[0]][new_pos[1]] == 0: 
                                        visited[new_pos[0]][new_pos[1]] = 1 
                                        q.append(new_pos)
            cur = (pos[0],pos[1],"")
            q.append(cur) 

        return res 

if __name__ == "__main__": 
    s = Solution() 

    target = "leet"
    print(s.alphabetBoardPath(target)) 
