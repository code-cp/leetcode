from sortedcontainers import SortedList

class ExamRoom:
    # (-1, n) means seats between -1 and n can be used
    # it's open range 
    def __init__(self, n: int): 
        def dist(l, r): 
            if l == -1 or r == n:
                return r - l - 1  
            else:
                return (r - l) // 2 
        self.n = n 
        self.sl = SortedList(key=lambda x: (-dist(*x), x[0]))
        # record occupied seats to the left and right for removal 
        self.left = {}
        self.right = {}
        
        self.add((-1, n))

    def add(self, x) -> None: 
        self.sl.add(x)
        self.left[x[1]] = x[0]
        self.right[x[0]] = x[1]

    def delete(self, x) -> None: 
        self.sl.remove(x)
        self.left.pop(x[1])
        self.right.pop(x[0])

    def seat(self) -> int:
        x = self.sl[0]
        pick = (x[0]+x[1]) // 2 
        if x[0] == -1: 
            pick = 0 
        elif x[1] == self.n: 
            pick = self.n - 1 
        self.delete(x)
        self.add((x[0], pick))
        self.add((pick, x[1]))
        return pick

    def leave(self, p: int) -> None:
        l, r = self.left[p], self.right[p]
        self.delete((l, p))
        self.delete((p, r))
        self.add((l, r))
