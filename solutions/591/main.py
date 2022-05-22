from typing import * 

# ref https://leetcode.com/problems/tag-validator/discuss/103374/C++-Clean-Code-Recursive-Parser
# tag :
#     <tagname> + content + </tagname>
# tagname : 
#     [A-Z]{1, 9}                 # 1 ~ 9 uppercase chars
# content : 
#     (tag|cdata|text)*           # 0 or more of : tag, cdata, text
# cdata : 
#     "<![CDATA[" + .* + "]]>"
# text :
#     [^<]+                       # non '<' chars

from collections import deque 
class Solution:
    def parseTag(self): 
        def validTag(tag): 
            if len(tag) > 9 or len(tag) < 1: 
                return False 
            for i in range(len(tag)): 
                if ord(tag[i]) < ord('A') or ord(tag[i]) > ord('Z'): 
                    return False 
            return True 

        if self.html[self.start_idx] != '<':
            return None 
        end_idx = self.start_idx
        while end_idx < self.str_len and self.html[end_idx] != '>':
            end_idx += 1 
        if end_idx == self.str_len:
            return None 
        tag = self.html[self.start_idx+1:end_idx] 
        if not validTag(tag): 
            return None 
        self.start_idx = end_idx + 1 
        return tag 

    def parseChar(self):
        end_idx = self.start_idx
        while end_idx < self.str_len and self.html[end_idx] != '<':
            end_idx += 1 
        if end_idx != self.start_idx: 
            self.start_idx = end_idx 
            return True 
        else: 
            return False 

    def parseCData(self): 
        if self.html[self.start_idx:].find("<![CDATA[") != 0:
            return False 
        end_idx = self.html[self.start_idx:].find("]]>") 
        if end_idx == -1: 
            return False 
        self.start_idx += end_idx + 3 
        return True  

    def validCode(self): 
        def validClosedTag(tag, tag_name): 
            if tag[0:2] == "</" and tag[-1] == ">" and tag[2:-1] == tag_name:
                return True 
            else: 
                self.stack.append(tag_name)
                return False 

        tag_name = self.parseTag()
        if tag_name is None: 
            return False 
        self.stack.append(tag_name)

        while self.start_idx < self.str_len:  
            if not self.parseChar() and not self.parseCData() and not self.validCode(): 
                break   

        tag_name = self.stack.pop()
        tag_end_idx = self.start_idx + len(tag_name) + 2 
        if tag_end_idx >= self.str_len: 
            return False 
        if not validClosedTag(self.html[self.start_idx:tag_end_idx+1], tag_name):
            return False 
        self.start_idx = tag_end_idx + 1 
        return True 

    def isValid(self, code: str) -> bool:
        self.html = code 
        self.str_len = len(code) 
        self.start_idx = 0 
        self.stack = deque()
        if not self.validCode():
            return False 
        if self.start_idx != self.str_len: 
            return False 
        return True 

if __name__ == "__main__": 
    s = Solution()

    code = "<DIV>This is the first line <![CDATA[<div>]]></DIV>"
    assert s.isValid(code) 
    code = "<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>"
    assert s.isValid(code) 
    code = "<A>  <B> </A>   </B>"
    assert not s.isValid(code) 
    code = "<A><A>/A></A></A>"
    assert s.isValid(code)
    code = "<A><B><![CDATA[></B>]]></A>"
    assert not s.isValid(code) 