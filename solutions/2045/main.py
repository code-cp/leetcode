from typing import List 
from collections import defaultdict

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # build graph
        next_matrix = defaultdict(set)
        for e in edges:
            next_matrix[e[0]].add(e[1])
            next_matrix[e[1]].add(e[0])

        # from 1 to n, 0 not used
        visitied = [0] * (n+1)
        dist = [-float("inf")] * (n+1)
        my_queue = []
        # node, time
        my_queue.append([1, 0])
        dist[1] = 0
        visitied[1] = 1

        # bfs
        while len(my_queue) > 0:
            cur = my_queue.pop(0)
            # // is Floor Division
            cur_round = cur[1] // change
            if cur_round % 2 == 1:
                # red light
                cur_time = (cur_round + 1) * change + time
            else:
                # green light
                cur_time = cur[1] + time

            for neighbor in next_matrix[cur[0]]:
                # only update when dist[neighbor] < cur_time, since
                # we are looking for the second min
                if visitied[neighbor] < 2 and dist[neighbor] < cur_time:
                    visitied[neighbor] += 1
                    if visitied[neighbor] == 2 and neighbor == n:
                        return cur_time

                    dist[neighbor] = cur_time
                    my_queue.append([neighbor, cur_time])

        return 0

if __name__ == "__main__": 
    n = 5
    edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]
    time = 3
    change = 5
    s = Solution()
    assert s.secondMinimum(n, edges, time, change) == 13
