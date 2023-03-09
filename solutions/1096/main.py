from typing import * 

class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        strs = set()
        
        def dfs(exp): 
            end = exp.find("}")
            if end == -1: 
                strs.add(exp)
                return 
            start = exp.rfind("{", 0, end-1)
            prefix, suffix = exp[:start], exp[end+1:]
            for cur_str in exp[start+1:end].split(","):
                dfs(prefix+cur_str+suffix)
            
        dfs(expression)
        return sorted(strs)