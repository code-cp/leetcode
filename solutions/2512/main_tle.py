from typing import * 

class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        students_info = []
        n = len(report)
        
        for i in range(n): 
            words = report[i].split()
            score = 0
            for w in words:
                if w in positive_feedback: 
                    score += 3 
                elif w in negative_feedback: 
                    score -= 1 
            students_info.append((score, student_id[i]))
            
        students_info.sort(key=lambda x: (x[0], -x[1]), reverse=True)
        
        ans = [x[1] for x in students_info]
        
        return ans[:k]
            
            
        