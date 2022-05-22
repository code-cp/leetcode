from typing import * 

# this problem tests how to implement comparator for a sorting algorithm 

# https://leetcode-cn.com/problems/reorder-data-in-log-files/solution/zhong-xin-pai-lie-ri-zhi-wen-jian-by-lee-egtm/1541852
# 如果b[0].isalpha()，说明是letter，返回(0, b, a)意思是把letter放前面，然后按照b排序，b相等的话按照a排序，a是identifier。如果不是letter，题目说digit保持位置不变，所以不需要排序，返回(1, )。
# 这里需要sort是稳定的，就是说在输入的关键字相同的情况下，输入的顺序和输出的顺序是一致的，Python里sort是稳定的，所以可以都返回(1, )。

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def comp(log: str) -> tuple: 
            # maxsplit : It is a number, which tells us to split the string into maximum of provided number of times. 
            # If it is not provided then the default is -1 that means there is no limit
            # ref https://www.geeksforgeeks.org/python-string-split/
            a, b = log.split(' ', 1) 
            
            # if b[0].isalpha(), means it is Letter-log, then we need to put it in front 
            # and we need to compare the content first, then compare the identifier 
            # else, it is digit-log, then we do not need to sort, so return (1, )
            
            # sort is stable, so we can just use (1, ) here 
            return (0, b, a) if b[0].isalpha() else (1, )
            # in case sort is unstable, then need to sort (log, index) 
        
        logs.sort(key=comp)
        return logs 

if __name__ == "__main__": 
    s = Solution()

    logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    result = s.reorderLogFiles(logs) 
    assert result == ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]