from typing import * 
from collections import defaultdict
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        res = []
        folders = defaultdict(int)
        for n in names: 
            if folders[n] == 0:
                res.append(n)
                folders[n] += 1 
            else: 
                idx = folders[n]
                while n+f"({str(idx)})" in folders: 
                    idx += 1 
                res.append(n+f"({str(idx)})")
                folders[n] = idx + 1 
                folders[n+f"({str(idx)})"] = 1 
        return res 

if __name__ == "__main__":
    s = Solution() 

    names = ["kaido","kaido(1)","kaido","kaido(1)","kaido(2)"]
    assert s.getFolderNames(names) == ["kaido","kaido(1)","kaido(2)","kaido(1)(1)","kaido(2)(1)"]

    # names = ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]
    # assert s.getFolderNames(names) == ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece(4)"]
