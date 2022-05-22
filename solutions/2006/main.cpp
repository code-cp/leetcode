#include <unordered_map>
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int countKDifference(vector<int>& nums, int k) {
        unordered_map<int, int> umap; 
        int result = 0; 
        for (const auto& n : nums) {
            result += umap[n]; 
            umap[n+k]++;
            umap[n-k]++;
        }
        return result; 
    }
};

TEST(Test2006, SimpleTest) {
    vector<int> nums{1,2,2,1}; 
    const int k = 1; 
    Solution s; 
    EXPECT_EQ(s.countKDifference(nums, k), 4); 
}

int main() {
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS(); 
}