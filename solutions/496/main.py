from typing import List 

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreatInd = [-1] * len(nums2)
        # stack
        st = []
        st.append(0)
        for i in range(1, len(nums2)):
            if nums2[st[-1]] < nums2[i]:
                while len(st) > 0 and nums2[st[-1]] < nums2[i]:
                    nextGreatInd[st[-1]] = i
                    st = st[:-1]
            st.append(i)
        result = []
        for n in nums1:
            ind = nextGreatInd[nums2.index(n)]
            if ind != -1:
                result.append(nums2[ind])
            else:
                result.append(-1)
        return result

if __name__ == "__main__": 
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    s = Solution()
    print(s.nextGreaterElement(nums1, nums2))
