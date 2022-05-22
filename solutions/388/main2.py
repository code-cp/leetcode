from collections import deque
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        res = 0 
        stack = deque()
        pre_level, cur_level = -1, -1 
        dirs = input.split("\n")
        for d in dirs: 
            cur_level = 0
            while d[cur_level] == '\t': 
                cur_level += 1
            while cur_level <= pre_level: 
                stack.pop()
                pre_level -= 1 
            pre_level = cur_level
            valid_len = len(d[cur_level:])
            stack.append(valid_len)
            if '.' in d: 
                cur_len = 0 
                for s in stack: 
                    cur_len += s + 1
                res = max(res, cur_len-1) 
        return res 

if __name__ == "__main__": 
    s = Solution()

    input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    result = s.lengthLongestPath(input)
    assert result == 32 

    result = s.lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")
    assert result == 20 