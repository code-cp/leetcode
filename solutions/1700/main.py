from typing import * 

from collections import deque 
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stu_q = deque()
        for s in students: 
            stu_q.appendleft(s)
        j = 0 
        continue_flag = True 
        while continue_flag: 
            stu_len = len(stu_q)
            continue_flag = False 
            for _ in range(stu_len):
                if sandwiches[j] == stu_q[0]: 
                    j += 1 
                    stu_q.popleft()
                    continue_flag = True 
                else: 
                    s = stu_q.popleft()
                    stu_q.append(s)
        return len(stu_q)

if __name__ == "__main__": 
    s = Solution()

    students = [1,1,1,0,0,1]
    sandwiches = [1,0,0,0,1,1]
    assert s.countStudents(students, sandwiches) == 3

    students = [1,1,0,0]
    sandwiches = [0,1,0,1]
    assert s.countStudents(students, sandwiches) == 0 
            

