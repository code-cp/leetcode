from typing import * 

# this problem tests how to implement comparator for a sorting algorithm 
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def comp(log_idx: tuple) -> tuple: 
            log, idx = log_idx[0], log_idx[1]
            a, b = log.split(' ', 1) 
            return (0, b, a) if b[0].isalpha() else (1, idx)
        
        logs_idx = [(log, idx) for idx, log in enumerate(logs)]
        logs_idx.sort(key=comp)
        logs = [log for log, idx in logs_idx]
        return logs 

if __name__ == "__main__": 
    s = Solution()

    logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    result = s.reorderLogFiles(logs) 
    assert result == ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]