from collections import defaultdict  
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        res = 0 
        path_level = defaultdict(lambda:-1) 
        dirs = input.split('\n') 
        for d in dirs: 
            level = 0 
            for c in d: 
                if c == '\t': 
                    level += 1 
            valid_len = len(d[level:])
            if '.' not in d: 
                path_level[level] = path_level[level-1] + 1 + valid_len
            else: 
                res = max(res, path_level[level-1] + 1 + valid_len)
        return res 

if __name__ == "__main__": 
    s = Solution()

    result = s.lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")
    assert result == 20 