from typing import List 

class Solution:
    def reverseBits(self, n: int) -> int:
        st = []
        result = 0
        for i in range(32):
            if n & 1:
                st.append(1)
            else:
                st.append(0)
            n = n >> 1
        for i in range(32):
            result |= st[-1] << i
            st.pop()
        return result

if __name__ == '__main__':
    n = 43261596
    s = Solution()
    assert s.reverseBits(n) == 964176192
