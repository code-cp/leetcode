from typing import List 

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # sort based on h
        # if h is same, sort based on k
        people.sort(key=lambda x: (-x[0], x[1]))
        que = []
        for p in people:
            que.insert(p[1], p)
        return que

if __name__ == "__main__":
    mySol = Solution()
    people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    print(mySol.reconstructQueue(people))
