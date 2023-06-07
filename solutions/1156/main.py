from collections import Counter 

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        cnt = Counter(text)
        n = len(text)
        
        skipped = 0 
        cur_letter = text[0]
        cur_cnt = 1
        
        max_cnt = 0 
        i = 1
        j = 0 
         
        while i < n: 
            t = text[i]
            if t == cur_letter:
                cur_cnt += 1 
            elif skipped == 0: 
                skipped += 1 
                j = i 
            else: 
                if cnt[cur_letter] > cur_cnt: 
                    cur_cnt += 1 
                if cur_cnt > max_cnt: 
                    max_cnt = cur_cnt
                
                # 从上一次断掉的地方重新开始计数
                if j > 0: 
                    i = j
                cur_letter = text[i] 
                skipped = 0 
                cur_cnt = 1 
            i += 1 
                
        # 如果skipped==1，那就替换中间的字母
        # 如果skipped==0，就替换之前的或者之后的一个字母
        if cnt[cur_letter] > cur_cnt: 
            cur_cnt += 1 
        if cur_cnt > max_cnt: 
            max_cnt = cur_cnt

        return max_cnt 
    
if __name__ == "__main__": 
    s = Solution() 
    
    # assert s.maxRepOpt1("aaaaa") == 5
    # assert s.maxRepOpt1("aaabaaa") == 6 
    # assert s.maxRepOpt1("ababa") == 3 
    # assert s.maxRepOpt1("aaabbaaa") == 4                    
    # assert s.maxRepOpt1("aabaaabaaaba") == 7 
    # assert s.maxRepOpt1("bbababaaaa") == 6 
    assert s.maxRepOpt1("acbaaa") == 4  