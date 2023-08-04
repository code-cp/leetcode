from typing import * 
from collections import deque 

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        stack = deque()
        tmp = ""
        for i, s in enumerate(source): 
            if "*/" in s and len(stack) > 0: 
                source[i] = tmp + s[s.index("*/")+2:]
                tmp = ""
                stack.pop()
                continue 
            if len(stack) > 0 and stack[-1] == "/*": 
                source[i] = ""
                continue
                
            if "*/" in s and "/*" in s:  
                if ("*/" in s and "/*" in s) and ("//" in s):  
                    if s.index("/*") > s.index("//"):
                        continue 
                start = s[:s.index("/*")] 
                left = s[s.index("/*")+2:]
                source[i] = start + left[left.index("*/")+2:]
                continue 
            if len(stack) == 0 and "/*" in s:  
                if ("*/" in s and "/*" in s) and ("//" in s):  
                    if s.index("/*") > s.index("//"):
                        continue 
                stack.append("/*")
                tmp = s[:s.index("/*")]
                source[i] = ""
                continue 
                
            if "//" in s: 
                source[i] = s[:s.index("//")]
                continue 
            
        source = [s for s in source if len(s) > 0]
        return source
    
if __name__ == "__main__": 
    s = Solution()
    
    # assert s.removeComments(["class test{", "public: ", "   int x = 1;", "   /*double y = 1;*/", "   char c;", "};"]) == ["class test{","public: ","   int x = 1;","   ","   char c;","};"]
    # assert s.removeComments(["a/*comment", "line", "more_comment*/b"]) == ["ab"]
    # assert s.removeComments(["struct Node{", "    /*/ declare members;/**/", "    int size;", "    /**/int val;", "};"]) == ["struct Node{","    ","    int size;","    int val;","};"]
    assert s.removeComments(["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]) == ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]
    # assert s.removeComments(["main() {", "  Node* p;", "  /* declare a Node", "  /*float f = 2.0", "   p->val = f;", "   /**/", "   p->val = 1;", "   //*/ cout << success;*/", "}", " "]) == ["main() {","  Node* p;","  ","   p->val = 1;","   ","}"," "]
    # assert s.removeComments(["a/*/b//*c","blank","d//*e/*/f"]) == ["af"]