# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/count-unique-characters-of-all-substrings-of-a-given-string/solution/by-endlesscheng-ko4z/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        ans = total = 0 
        last0, last1 = {}, {}
        for i, c in enumerate(s): 
            # total records the number of substrings end at i 
            total += (i - last0.get(c, -1)) - (last0.get(c, -1) - last1.get(c, -1))
            # ans records the number of substrings end at every i 
            ans += total 
            last1[c] = last0.get(c, -1)
            last0[c] = i 
        return ans 



if __name__ == "__main__": 
    s = Solution()

    input_str = "ABC"
    assert s.uniqueLetterString(input_str) == 10 