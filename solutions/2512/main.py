from typing import * 

class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        students_info = []

        positive_score = {}
        for p in positive_feedback: 
            positive_score[p] = 3 
        negative_score = {}
        for n in negative_feedback: 
            negative_score[n] = -1 

        n = len(report)
        
        for i in range(n): 
            words = report[i].split()
            score = 0
            for w in words:
                score += positive_score.get(w, 0)
                score += negative_score.get(w, 0)
            students_info.append((score, student_id[i]))
            
        students_info.sort(key=lambda x: (x[0], -x[1]), reverse=True)
        
        ans = [x[1] for x in students_info]
        
        return ans[:k]
            
            
        