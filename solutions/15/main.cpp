#include <algorithm>
#include <numeric>
#include <vector>
#include <gtest/gtest.h>

using namespace std; 

// use double pointers 
// time complexity O(n^2)
// space complexity O(1)
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        
        vector<vector<int> > result; 
        
        // check input size 
        if (nums.size() < 3)
            return result;
        
        sort(nums.begin(), nums.end());
        
        const int target = 0; 
        
        for (auto i = nums.begin(); i < nums.end() - 2; ++i) 
        {
            auto j = i + 1; 
            
            // skip duplicates 
            if (i > nums.begin() && *i == *(i-1))
                continue; 
                
            auto k = nums.end() - 1;
            
            while (j < k) 
            {
                if (*i + *j + *k < target) 
                {
                    ++j; 
                    // skip duplicates
                    while (*j == *(j - 1) && j < k)
                        ++j; 
                }
                else if (*i + *j + *k > target) 
                {
                    --k; 
                    // skip duplicates 
                    while (*k == *(k + 1) && j < k)
                        --k; 
                }
                else 
                {
                    result.push_back({*i, *j, *k});
                    ++j; 
                    --k; 
                    // skip duplicates
                    while (*j == *(j - 1) && j < k)
                        ++j; 
                    while (*k == *(k + 1) && j < k)
                        --k; 
                }
            }
        }
        return result; 
    }
};

TEST(Test15, SimpleTest)
{
    vector<int> nums = {-1,0,1,2,-1,-4};
    Solution s; 
    vector<vector<int>> results = s.threeSum(nums); 
    for (const auto& result : results)
    {
        EXPECT_EQ(accumulate(result.begin(), result.end(), 0), 0) << "Wrong answer"; 
    }
}

int main() 
{
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS(); 
}
