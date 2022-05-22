#include <iostream>
#include <unordered_map> 
#include <algorithm>
#include <numeric> 
#include <gtest/gtest.h>

using namespace std; 

// use multimap
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        
        vector<vector<int>> result; 
        
        // check input 
        if (nums.size() < 4)
            return result; 
        
        sort(nums.begin(), nums.end());
        
        unordered_multimap<int, pair<int, int>> cache; 
        
        for (size_t i = 0; i < nums.size() - 1; ++i)
        {
            for (size_t j = i + 1; j < nums.size(); ++j)
            {
                cache.insert(make_pair(nums[i] + nums[j], make_pair(i, j)));
            }
        }
                             
        for (auto i = cache.begin(); i != cache.end(); ++i)
        {
            int diff = target - i->first; 
            auto range = cache.equal_range(diff);
            for (auto j = range.first; j != range.second; ++j)
            {
                auto a = i->second.first; 
                auto b = i->second.second; 
                auto c = j->second.first; 
                auto d = j->second.second; 
                if (a != c && a != d && b != c && b != d) 
                {
                    vector<int> vec = {nums[a], nums[b], nums[c], nums[d]};
                    sort(vec.begin(), vec.end());
                    result.push_back(vec);
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
