from typing import * 

# wrong 
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        count = 0 
        n = len(ideas)
        names = set()
        for i in range(n-1): 
            for j in range(i+1, n): 
                a, b = list(ideas[i]), list(ideas[j])
                print(f"a {a} b {b}")
                if a == b: 
                    continue 
                a[0], b[0] = b[0], a[0]
                a = "".join(a)
                b = "".join(b)
                if a not in ideas and a not in names: 
                    count += 1 
                    names.add(a)
                if b not in ideas and b not in names: 
                    count += 1 
                    names.add(b)
        return count

if __name__ == "__main__": 
    s = Solution()

    ideas = ["coffee","donuts","time","toffee"]
    assert s.distinctNames(ideas) == 6 