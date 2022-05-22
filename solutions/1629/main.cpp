/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sun Jan  9 09:33:10 2022
> Description:   
 ************************************************************************/
#include <string> 
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    char slowestKey(vector<int>& releaseTimes, string keysPressed) {
        char result;
        int maxTime = 0, time = 0;
        for (int i = 0; i < releaseTimes.size(); ++i) {
            if (i == 0) time = releaseTimes[i];
            else time = releaseTimes[i] - releaseTimes[i-1];
            if (time > maxTime) {
                maxTime = time;
                result = keysPressed[i];
            }
            else if (time == maxTime) {
                if (result < keysPressed[i]) result = keysPressed[i];
            }
        }
        return result;
    }
};

TEST(Test1629, SimpleTest) {
    vector<int> releaseTimes = {9,29,49,50};
    string keysPressed = "cbcd";
    Solution s; 
    EXPECT_EQ(s.slowestKey(releaseTimes, keysPressed), 'c');
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
