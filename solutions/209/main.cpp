#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

// sliding window 
// time complexity O(n), since each element is processed twice 
// once in window, once out of window 
// space complexity O(1)
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int result = INT32_MAX;
        int sum = 0; 
        int left = 0; 
        int subLength = 0; 
        for (int right = 0; right < nums.size(); ++right) {
            sum += nums[right];
            // note here we use a while loop  
            while (sum >= target) {
                subLength = right - left + 1; 
                result = result > subLength ? subLength : result; 
                sum -= nums[left++]; 
            }
        }
        return result == INT32_MAX ? 0 : result; 
    }
};

TEST(Test209, SimpleTest)
{
    vector<int> nums = {2,3,1,2,4,3};
    const int target = 7; 
    Solution s; 
    int result = s.minSubArrayLen(target, nums); 
    EXPECT_EQ(result, 2) << "Wrong answer"; 
}

int main() 
{
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}