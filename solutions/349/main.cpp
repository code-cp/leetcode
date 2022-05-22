#include <unordered_set> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        // note since the answer requires unique elements, need to use unordered_set
        // instead of vector 
        unordered_set<int> result; 
        unordered_set<int> nums1_set(nums1.begin(), nums1.end());
        for (const auto& n : nums2) {
            if (nums1_set.find(n) != nums1_set.end()) {
                result.insert(n); 
            }
        }
        return vector<int>(result.begin(), result.end()); 
    }
};

TEST(Test349, SimpleTest) {
    vector<int> nums1 = {1,2,2,1};
    vector<int> nums2 = {2, 2}; 
    Solution s; 
    vector<int> result = s.intersection(nums1, nums2); 
    EXPECT_EQ(result[0], 2); 
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}