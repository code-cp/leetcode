#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int countGoodRectangles(vector<vector<int>>& rectangles) {
        int max_len = INT_MIN, result = 0;
        int min_side;  
        for (const auto& r: rectangles) {
            min_side = min(r[0], r[1]);
            if (max_len < min_side) {
                max_len = min_side; 
                result = 1; 
            }
            else if (max_len == min_side) result++; 
        }
        return result; 
    }
};

TEST(Test1725, SimpleTest) {
    Solution s; 
    vector<vector<int>> rectangles = {{5,8}, {3,9}, {5,12}, {16,5}};
    EXPECT_EQ(s.countGoodRectangles(rectangles), 3); 
}

int main() {
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS(); 
}