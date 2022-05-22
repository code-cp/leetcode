/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Mon Nov 15 14:31:25 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        long int diff = 0;
        vector<int> result(2, 0);
        for (const auto& n : nums)
            diff ^= n;
        // note, cannot use diff ^ -diff
        diff = diff & -diff;
        for (const auto& n : nums) {
            // note, cannot use n ^ diff
            if (n & diff)
                result[0] ^= n;
            else
                result[1] ^= n;
        }
        return result;
    }
};

TEST(Test260, SimpleTest) {
    vector<int> nums{
        1,2,1,3,2,5
    };
    Solution s; 
    vector<int> result = s.singleNumber(nums);
    for (auto& r : result)
        cout << r << " ";
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
