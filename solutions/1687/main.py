from typing import * 

class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        n = len(boxes)
        boxes.insert(0, [-1, 0])
        dp = [float("inf")]*(n+1)
        dp[0] = 0 

        trip_num = 0 
        last_port = last_j = -1  

        j = 0
        weight_sum = 0  
        for i in range(1, n+1): 
            # plan 1 greedy 
            while j+1 <= n and (j+1-i+1) <= maxBoxes and weight_sum+boxes[j+1][1] <= maxWeight: 
                j += 1 
                weight_sum += boxes[j][1]
                if boxes[j][0] != boxes[j-1][0]: 
                    trip_num += 1
                # record the index of last visited port 
                if boxes[j][0] != last_port: 
                    last_port = boxes[j][0]
                    last_j = j 

            # finalize [i, j] 
            # dp[j] = dp[i-1] + numTrips(i, j) + 1
            dp[j] = min(dp[j], dp[i-1] + trip_num + 1)

            # plan 2 if ports are same 
            if j+1 <= n and boxes[j][0] == boxes[j+1][0]: 
                # dp[j'] = min(dp[j'], dp[i-1] + trip_num - 1 + 1) 
                dp[last_j-1] = min(dp[last_j-1], dp[i-1] + trip_num)
            
            # update interval 
            weight_sum -= boxes[i][1]
            if i+1 <= n and boxes[i][0] != boxes[i+1][0]: 
                trip_num -= 1 

        return dp[-1]

if __name__ == "__main__": 
    s = Solution() 

    boxes = [[1,1],[2,1],[1,1]]
    portsCount = 2
    maxBoxes = 3
    maxWeight = 3
    assert s.boxDelivering(boxes, portsCount, maxBoxes, maxWeight) == 4 