from typing import * 

import heapq 

# TLE 
# https://leetcode-cn.com/submissions/detail/292094052/testcase/
class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        result = [] 
        server_load = [0] * k 
        # 1 is available, 0 is busy 
        available_servers = [1] * k 
        task_end_heap = []
        for i, a in enumerate(arrival): 
            # free the servers 
            while len(task_end_heap) > 0: 
                (end_time, server) = heapq.heappop(task_end_heap)
                if end_time <= a: 
                    available_servers[server] = 1
                else: 
                    heapq.heappush(task_end_heap, (end_time, server))
                    break 
            # assign the new request 
            server = i % k 
            if available_servers[server]:
                available_servers[server] = 0 
                heapq.heappush(task_end_heap, (a + load[i], server)) 
                server_load[server] += 1 
            else: 
                if sum(available_servers) == 0: 
                    # all servers are busy 
                    # drop the request 
                    continue 
                j = (server + 1) % k  
                while j != server and not available_servers[j]:
                    j += 1 
                    j %= k 
                server = j
                if available_servers[server]: 
                    available_servers[server] = 0 
                    heapq.heappush(task_end_heap, (a + load[i], server)) 
                    server_load[server] += 1
                else: 
                    # drop the request 
                    continue 
        max_load = max(server_load)
        result = [i for i, x in enumerate(server_load) if x == max_load]
        return result 

if __name__ == "__main__": 
    s = Solution() 

    k = 3
    arrival = [1,2,3,4,5]
    load = [5,2,3,3,3] 
    result = s.busiestServers(k, arrival, load) 
    assert result == [1]

    k = 3
    arrival = [1,2,3,4]
    load = [1,2,1,2]
    result = s.busiestServers(k, arrival, load) 
    assert result == [0]