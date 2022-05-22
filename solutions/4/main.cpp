#include <iostream>
#include <vector>
#include <gtest/gtest.h>

using namespace std; 

class Solution {
private:
        // When we declare a member of a class as static it means no matter how many objects of the class are created, there is only one copy of the static member.
        static int find_kth(std::vector<int>::const_iterator A, int m, std::vector<int>::const_iterator B, int n, int k) {
            // assume m is equal or smaller than n 
            if (m > n)
                return find_kth(B, n, A, m, k);
            
            // check whether one of arrays is empty 
            if (m == 0)
                return *(B + k - 1); 
            
            // check if we want the min 
            if (k == 1)
                return min(*A, *B); 
            
            // divide k into two parts, delete unnecessary ones 
            int ia = min(k / 2, m), ib = k - ia; 
            if (*(A + ia - 1) < *(B + ib - 1))
                return find_kth(A + ia, m - ia, B, n, k - ia); 
            else if (*(A + ia - 1) > *(B + ib - 1))
                return find_kth(A, m, B + ib, n - ib, k - ib);
            else 
                return A[ia - 1];
        }
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        const int m = nums1.size();
        const int n = nums2.size(); 
        
        int total = m + n; 
        if (total & 0x1)
            // if total number is odd 
            return find_kth(nums1.begin(), m, nums2.begin(), n, total / 2 + 1);
        else 
            // total number is even 
            return (find_kth(nums1.begin(), m, nums2.begin(), n, total / 2) + 
                   find_kth(nums1.begin(), m, nums2.begin(), n, total / 2 + 1)) / 2.0; 
    }
};

TEST(Test4, SimpleTest)
{
    vector<int> nums1 = {1, 3};
    vector<int> nums2 = {2}; 
    Solution s; 
    EXPECT_EQ(s.findMedianSortedArrays(nums1, nums2), 2.0) << "Wrong results, should be 2.0";
}

int main() {
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS();
}
