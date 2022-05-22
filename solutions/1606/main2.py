from typing import * 

import heapq

class Solution:
    def nextServer(self, server, available_servers, insert=False): 
        n = len(available_servers)
        if n == 0: 
            if insert:
                available_servers.append(server)
            return -1 
        if not insert and (server > available_servers[-1] or server < available_servers[0]): 
            server = available_servers[0]
            available_servers.remove(server)
            return server 
        left, right = 0, n-1
        while left <= right: 
            mid = left + (right - left) // 2 
            if available_servers[mid] == server: 
                available_servers.remove(server) 
                return server 
            elif available_servers[mid] > server: 
                right = mid - 1
            else: 
                left = mid + 1 
        if available_servers[mid] > server: 
            if insert: 
                available_servers.insert(mid, server)
            else: 
                server = available_servers[mid]
                available_servers.remove(server) 
            return server
        else: 
            if insert: 
                available_servers.insert(mid+1, server)
            else: 
                server = available_servers[(mid+1)%n]
                available_servers.remove(server)
            return server 

    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        result = [] 
        server_load = [0] * k 
        # 1 is available, 0 is busy 
        available_servers = list(range(k))
        task_end_heap = []
        for i, a in enumerate(arrival): 
            # free the servers 
            while len(task_end_heap) > 0: 
                (end_time, server) = heapq.heappop(task_end_heap)
                if end_time <= a: 
                    self.nextServer(server, available_servers, insert=True)
                else: 
                    heapq.heappush(task_end_heap, (end_time, server))
                    break 
            # assign the new request 
            server = i % k 
            server = self.nextServer(server, available_servers)
            if server != -1:
                heapq.heappush(task_end_heap, (a + load[i], server)) 
                server_load[server] += 1 
            else: 
                # cannot assign server, drop the request  
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

    k = 7
    arrival = [1,3,4,5,6,11,12,13,15,19,20,21,23,25,31,32]
    load = [9,16,14,1,5,15,6,10,1,1,7,5,11,4,4,6]
    result = s.busiestServers(k, arrival, load) 
    assert result == [0]

    k = 13
    arrival = [1,3,6,7,8,9,10,14,16,20,21,24,25,28,29,30,33,34]
    load = [20,27,27,14,14,9,15,8,23,1,34,2,28,25,7,6,24,15]
    result = s.busiestServers(k, arrival, load) 
    assert result == [0,3,4,5,6]