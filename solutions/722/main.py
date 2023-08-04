from typing import * 
from collections import deque 
import math 
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        in_block_comment = False 
        new_line = []
        for s in source:
            s = list(s)
            if len(s) > 0 and not in_block_comment: 
                new_line.append(s[0])
            i = 1 
            while i < len(s): 
                sym = "".join(s[i-1:i+1])
                if not in_block_comment and sym == "//": 
                    if len(new_line) > 0: 
                        # remove "/"
                        new_line.pop()
                    break 
                elif in_block_comment and sym == "*/":
                    # prevent *//
                    s[i] = "?"
                    in_block_comment = False 
                elif not in_block_comment and sym == "/*": 
                    # prevent /*/ 
                    s[i] = "?"
                    in_block_comment = True 
                    if len(new_line) > 0: 
                        # remove "/"
                        new_line.pop()
                elif not in_block_comment: 
                    new_line.append(s[i])
                i += 1 
            if len(new_line) > 0 and not in_block_comment:
                res.append("".join(new_line))
                new_line = []
        return res 
    
if __name__ == "__main__": 
    s = Solution()
    
    assert s.removeComments(["class test{", "public: ", "   int x = 1;", "   /*double y = 1;*/", "   char c;", "};"]) == ["class test{","public: ","   int x = 1;","   ","   char c;","};"]
    assert s.removeComments(["a/*comment", "line", "more_comment*/b"]) == ["ab"]
    assert s.removeComments(["struct Node{", "    /*/ declare members;/**/", "    int size;", "    /**/int val;", "};"]) == ["struct Node{","    ","    int size;","    int val;","};"]
    assert s.removeComments(["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]) == ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]
    assert s.removeComments(["main() {", "  Node* p;", "  /* declare a Node", "  /*float f = 2.0", "   p->val = f;", "   /**/", "   p->val = 1;", "   //*/ cout << success;*/", "}", " "]) == ["main() {","  Node* p;","  ","   p->val = 1;","   ","}"," "]
    assert s.removeComments(["a/*/b//*c","blank","d//*e/*/f"]) == ["af"]
    assert s.removeComments(["a//*b/*/c","blank","d/*/e/*/f"]) == ["a","blank","df"]
    assert s.removeComments(["a/*/b//*c","blank","d/*/e*//f"]) == ["ae*"]
    assert s.removeComments(["a//*b//*c","blank","d*//e*//f"]) == ["a","blank","d*"]
    assert s.removeComments(["/*/bcbc//*ebdb/*/bab/*/a/*//*/d/*///*de/*///*d*//dc*///*/cd//*ccd//*a//*caacad"]) == ["bab"]