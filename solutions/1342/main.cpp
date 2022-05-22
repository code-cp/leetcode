#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int numberOfSteps(int num) {
        int result = 0; 
        while (num > 0) {
            if (num & 1) num -= 1; 
            else num >>= 1; 
            result++;
        }
        return result; 
    }
};

TEST(Test1342, SimpleTest) {
    const int num = 14; 
    Solution s; 
    EXPECT_EQ(s.numberOfSteps(num), 6); 
}

int main() {
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS(); 
}

