#include <iostream>
#include <vector> 
#include <algorithm>
#include <numeric> 
#include <gtest/gtest.h> 

using namespace std; 

// use double pointer 
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        
        vector<vector<int>> result; 
        
        // check input 
        if (nums.size() < 4)
            return result; 
        
        sort(nums.begin(), nums.end());
        
        for (auto i = nums.begin(); i < nums.end() - 3; ++i)
        {
            for (auto j = next(i); j < nums.end() - 2; ++j)
            {
                auto k = next(j);
                auto l = nums.end() - 1; 
                
                while (k < l)
                {
                    auto total_sum = *i + *j + *k + *l; 
                    if (total_sum < target)
                    {
                        ++k; 
                    }
                    else if (total_sum > target)
                    {
                        --l; 
                    }
                    else 
                    {
                        result.push_back({*i, *j, *k, *l});
                        ++k; 
                        --l; 
                    }
                }
            }
        }
        
        sort(result.begin(), result.end());
        result.erase(unique(result.begin(), result.end()), result.end());
        return result; 
    }
};

TEST(Test18, SimpleTest)
{
    vector<int> nums = {1,0,-1,0,-2,2};
    const int target = 0;
    Solution s; 
    vector<vector<int>> result = s.fourSum(nums, target);
    for (const auto r : result)
    {
	    EXPECT_EQ(accumulate(r.begin(), r.end(), 0), target) << "Wrong answer"; 
    }
}

int main() {
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS();
}
