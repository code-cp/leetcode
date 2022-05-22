#include <unordered_map> 
#include <gtest/gtest.h> 

using namespace std; 

// time complexity O(n)
// space complexity O(n)
class Solution {
public:
    int fourSumCount(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3, vector<int>& nums4) {
        int result = 0; 
        unordered_map<int, int> umap;

        for (const auto& n1 : nums1)
            for (const auto& n2 : nums2) 
                umap[n1 + n2]++;

        for (const auto& n3 : nums3) 
            for (const auto& n4 : nums4) {
                int diff = 0 - n3 - n4; 
                auto itr = umap.find(diff); 
                if (itr != umap.end())
                    // note here is not result++
                    result += umap[diff]; 
            } 
        
        return result; 
    }
};

TEST(Test454, SimpleTest) {
    vector<int> nums1 = {1, 2}; 
    vector<int> nums2 = {-2, -1}; 
    vector<int> nums3 = {-1, 2}; 
    vector<int> nums4 = {0, 2}; 
    Solution s; 
    int result = s.fourSumCount(nums1, nums2, nums3, nums4); 
    EXPECT_EQ(result, 2); 
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}