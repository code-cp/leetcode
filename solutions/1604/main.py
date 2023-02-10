from typing import * 

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def checkHour(v):
            count = 1
            cur_max = v[0]+60 
            n = len(v)
            i = 1 
            while i < n: 
                if v[i] <= cur_max: 
                    count += 1 
                elif count == 1: 
                    cur_max = v[i]+60 
                else: 
                    if i == n-1: 
                        break 
                    cur_max = v[i-1]+60 
                    i -= 1
                    count = 1 
                if count >= 3: 
                    return True 
                i += 1 
            return False 

        entries = {}
        n = len(keyName)
        for i in range(n):
            k = keyName[i]
            if entries.get(k, -1) == -1: 
                entries[k] = []
            t = keyTime[i]
            t = t.split(":")
            t = int(t[0])*60+int(t[1])
            entries[k].append(t)
        res = []
        for k, v in entries.items():
            v.sort()
            if checkHour(v): 
                res.append(k)
        res.sort()
        return res 

if __name__ == "__main__": 
    s = Solution() 

    # keyName = ["leslie","leslie","leslie","clare","clare","clare","clare"]
    # keyTime = ["13:00","13:20","14:00","18:00","18:51","19:30","19:49"]
    # assert s.alertNames(keyName, keyTime) == ["clare","leslie"]

    # keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"]
    # keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
    # assert s.alertNames(keyName, keyTime) == ["daniel"]

    # keyName = ["alice","alice","alice","bob","bob","bob","bob"]
    # keyTime = ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]
    # assert s.alertNames(keyName, keyTime) == ["bob"]
 
    keyName = ["a","a","a","a","a","a","b","b","b","b","b"]
    keyTime = ["23:27","03:14","12:57","13:35","13:18","21:58","22:39","10:49","19:37","14:14","10:41"]
    assert s.alertNames(keyName, keyTime) == ["a"]

