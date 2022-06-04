from typing import * 

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set() 
        for e in emails: 
            local, domain = e.split('@') 
            local = local.split('+')[0].replace('.', '')
            res.add(local + '@' + domain) 
        return len(res)

if __name__ == "__main__": 
    s = Solution() 

    emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    assert s.numUniqueEmails(emails) == 2 