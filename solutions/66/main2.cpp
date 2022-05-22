#include <iostream>
#include <vector>
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        add(digits, 1); 
        return digits; 
    }
private:
    void add(vector<int>& digits, int digit)
    {
        int carry = digit; 
        for (auto it = digits.rbegin(); it != digits.rend(); ++it)
        {
            *it += carry; 
            carry = *it / 10; 
            *it %= 10; 
        }
        if (carry > 0)
            digits.insert(digits.begin(), carry); 
    }
};

TEST(Test66, SimpleTest)
{
    vector<int> digits = {4,3,2,1};
    Solution s; 
    s.plusOne(digits);
    EXPECT_EQ(digits[0], 4);
    EXPECT_EQ(digits[1], 3);
    EXPECT_EQ(digits[2], 2);
    EXPECT_EQ(digits[3], 2);
}

int main()
{
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
