#include <vector>
#include <gtest/gtest.h>

using namespace std; 

// time complexity O(n) 
// space complexity O(n)
class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> result(nums.size(), 0); 
        // use double pointer 
        // for each position, the largest value can only be the negative one on the left side,
        // or the positive one on the right side 
        auto left = nums.begin();
        auto right = nums.rbegin();
        for (auto itr = result.rbegin(); itr != result.rend(); itr++) {
            auto ll = *left * *left;
            auto rr = *right * *right;
            if (ll >= rr) {
                *itr = ll;
                left++; 
            }
            else {
                *itr = rr; 
                // note, right is reverse iterator, should use ++ instead of -- 
                right++; 
            }
        }
        return result; 
    }
};

TEST(Test977, SimpleTest)
{
    vector<int> nums = {-4,-1,0,3,10};
    vector<int> ans = {0,1,9,16,100}; 
    Solution s; 
    vector<int> result = s.sortedSquares(nums); 
    for (int i = 0; i < ans.size(); i++) {
        EXPECT_EQ(ans[i], result[i]); 
    }
}

int main() 
{
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}