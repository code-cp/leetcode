#include <iostream> 
#include <vector> 
#include <numeric> 
#include <algorithm>
#include <gtest/gtest.h>

using namespace std; 

// use upper_bound
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        
        vector<vector<int>> result; 
        
        // check input 
        if (nums.size() < 4)
            return result; 
        
        sort(nums.begin(), nums.end());
        
        for (auto i = nums.begin(); i < nums.end() - 3; i = upper_bound(i, nums.end() - 3, *i))
        {
            for (auto j = i + 1; j < nums.end() - 2; j = upper_bound(j, nums.end() - 2, *j))
            {
                auto k = j + 1; 
                auto l = nums.end() - 1; 
                while (k < l)
                {
                    if (*i + *j + *k + * l < target)
                    {
                        k = upper_bound(k, l, *k); 
                    }
                    else if (*i + *j + *k + *l > target)
                    {
                        l = lower_bound(k, l, *l) - 1;
                    }
                    else  
                    {
                        result.push_back({*i, *j, *k, *l});
                        k = upper_bound(k, l, *k);
                        l = lower_bound(k, l, *l); 
                    }
                }
            }
        }
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

int main() 
{
    testing::InitGoogleTest();
    return RUN_ALL_TESTS(); 
}
