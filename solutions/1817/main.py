from typing import * 

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        user_action = {}
        user_uam = {}
        for l in logs: 
            if user_action.get(l[0], -1) == -1: 
                user_action[l[0]] = set()
            if l[1] not in user_action[l[0]]:
                user_action[l[0]].add(l[1])
                ac = len(user_action[l[0]])
                if user_uam.get(ac, -1) == -1:
                    user_uam[ac] = 0 
                if ac > 1:
                    user_uam[ac-1] -= 1 
                user_uam[ac] += 1 
        res = [0] * k
        for i in range(1, k+1):
            res[i-1] = user_uam.get(i, 0)
        return res 

if __name__ == "__main__": 
    s = Solution() 

    logs = [[283268890,14532],[283268891,14530],[283268889,14530],[283268892,14530],[283268890,14531]]
    k = 2
    assert s.findingUsersActiveMinutes(logs, k) == [3,1]

    # logs = [[0,5],[1,2],[0,2],[0,5],[1,3]]
    # k = 5
    # assert s.findingUsersActiveMinutes(logs, k) == [0,2,0,0,0]

