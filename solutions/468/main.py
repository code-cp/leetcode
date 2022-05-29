from typing import * 

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def checkLeadingZero(num: str) -> bool: 
            if len(num) > 1 and num[0] == '0': 
                return True 
            return False 

        q = queryIP.split('.') if '.' in queryIP else queryIP.split(':') 
        if len(q) == 4:
            for i in q:
                if not i.isdigit() or not 0 <= int(i) <= 255:
                    return "Neither"
                if checkLeadingZero(i):
                    return "Neither" 
            return "IPv4" 

        if len(q) == 8: 
            for w in q: 
                if len(w) < 1 or len(w) > 4: 
                    return "Neither" 
                for i in w:
                    if not (i.isdigit() or i.lower().isalpha()):
                        return "Neither"
                    if ord(i.lower()) > ord('f'):
                        return "Neither"
            return "IPv6" 

        return "Neither" 

if __name__ == "__main__": 
    s = Solution() 

    queryIP = "172.16.254.1"
    assert s.validIPAddress(queryIP) == "IPv4" 

    queryIP = "256.256.256.256"
    assert s.validIPAddress(queryIP) == "Neither" 

    queryIP = "00.0.0.0"
    assert s.validIPAddress(queryIP) == "Neither" 

    queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
    assert s.validIPAddress(queryIP) == "IPv6"

    queryIP = "2001:0db8:85a3:00000:0:8A2E:0370:7334"
    assert s.validIPAddress(queryIP) == "Neither" 

    queryIP = "20EE:FGb8:85a3:0:0:8A2E:0370:7334"
    assert s.validIPAddress(queryIP) == "Neither" 

