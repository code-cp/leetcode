#include <iostream> 
#include <functional> 
#include <vector>
#include <algorithm> 
#include <numeric> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
private:
    template<typename T>
    void nextPermutation(T first, T last)
    {
        // get a reversed range 
        const auto r_first = reverse_iterator<T>(last);
        const auto r_last = reverse_iterator<T>(first);
    
        // begin with second last element 
        auto pivot = next(r_first);
        
        // find pivot, which is the first element no less than successor 
        while (pivot != r_last && *pivot >= *prev(pivot))
        {
            ++pivot; 
        }
        
        // if no such element is found, then current seq is the largest 
        // rearrange to first permutation
        if (pivot == r_last)
        {
            reverse(r_first, r_last); 
            return; 
        }
        
        // scan from right to left, find the first element greater than pivot 
        auto change = find_if(r_first, pivot, [&pivot](auto element){return (element > *pivot);});
        
        swap(*change, *pivot);
        reverse(r_first, pivot);
        
        return; 
    }
public:
    void nextPermutation(vector<int>& nums) {
        
        nextPermutation(nums.begin(), nums.end());
        
    }
};

TEST(Test31, SimpleTest)
{
    vector<int> nums = {1,2,3};
    Solution s; 
    s.nextPermutation(nums); 
    EXPECT_EQ(nums[0], 1); 
    EXPECT_EQ(nums[1], 3);
    EXPECT_EQ(nums[2], 2); 
} 

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}

