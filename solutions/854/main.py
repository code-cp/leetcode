from collections import deque 

class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        myq = deque()
        myq.append(s1)
        mymap = {}
        mymap[s1] = 0 
        
        def findN(source, target): 
            res = [] 
            i = 0 
            while source[i] == target[i]: 
                i += 1 
            for j in range(i, len(source)): 
                if source[j] == target[i]: 
                    temp = list(source)
                    temp[i], temp[j] = temp[j], temp[i]
                    res.append("".join(temp))
            return res 
            
        
        # bfs 
        while myq: 
            s = myq.popleft()
            if s == s2: 
                return mymap[s]
            neighbours = findN(s, s2)
            for n in neighbours: 
                if n not in mymap: 
                    mymap[n] = mymap[s] + 1 
                    myq.append(n)
        
        

if __name__ == "__main__": 
    s = Solution() 

    s1 = "ab"
    s2 = "ba"
    assert s.kSimilarity(s1, s2) == 1 

