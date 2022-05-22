#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <numeric> 
#include <gtest/gtest.h> 

using namespace std; 

// use unordered_map
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        
        vector<vector<int>> result; 
        
        // check input 
        if (nums.size() < 4)
            return result; 
        
        sort(nums.begin(), nums.end());
        
        unordered_map<int, vector<pair<int, int>>> cache; 
        
        for (size_t i = 0; i < nums.size() - 1; ++i)
        {
            for (size_t j = i + 1; j < nums.size(); ++j)
            {
                cache[nums[i] + nums[j]].push_back(pair<int, int>(i, j));
            }
        }
        
        for (size_t k = 0; k < nums.size() - 1; ++k)
        {
            for (size_t l = k + 1; l < nums.size(); ++l) 
            {
                int key = target - nums[k] - nums[l];
                if (cache.find(key) == cache.end())
                    continue; 
                const auto & vec = cache[key]; 
                for (const auto & v : vec)
                {
                    if (k <= v.second)
                        continue; 
                    result.push_back({nums[v.first], nums[v.second], nums[k], nums[l]});
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

int main()
{
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
