#include <vector> 
#include <algorithm> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int sumOfUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end()); 
        int result = 0, i = 0, j = 1; 
        while (i < nums.size()) {
            while (j < nums.size() && nums[j] == nums[i]) {j++;} 
            if (j - i == 1) {
                result += nums[i];
                i++; j++; 
            } 
            else {
                i = j; j++; 
            }
        }
        return result; 
    }
};

TEST(Test1748, SimpleTest) {
    vector<int> nums{1,2,3,2}; 
    Solution s; 
    EXPECT_EQ(s.sumOfUnique(nums), 4); 
}

int main() {
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS(); 
}