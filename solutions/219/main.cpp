/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Wed Jan 19 09:06:16 2022
> Description:   
 ************************************************************************/
#include <vector> 
#include <set> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        set<int> my_set;
        for (int i = 0; i < nums.size(); ++i) {
            if (my_set.find(nums[i]) != my_set.end()) return true;
            my_set.insert(nums[i]);
            if (i >= k) my_set.erase(nums[i-k]);
        }
        return false;
    }
};

TEST(Test219, SimpleTest) {
    vector<int> nums{
        1,2,3,1
    };
    const int k = 3; 
    Solution s;
    EXPECT_TRUE(s.containsNearbyDuplicate(nums, k));
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
    return RUN_ALL_TESTS();
}
