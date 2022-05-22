#include <iostream>
#include <vector>
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int carry = 0, temp = 0; 
        for (int i = digits.size() - 1; i >= 0; --i)
        {
            if (i == digits.size() - 1)
                temp = digits[i] + 1 + carry; 
            else 
                temp = digits[i] + carry; 

            carry = 0; 
            if (temp == 10)
            {
                digits[i] = 0; 
                ++carry;  
            } 
            else 
                digits[i] = temp; 
        }

        if (carry > 0)
            digits.insert(digits.begin(), carry);

        return digits; 
    }
};

TEST(Test66, SimpleTest)
{
    vector<int> digits = {1,2,3};
    Solution s; 
    s.plusOne(digits);
    EXPECT_EQ(digits[0], 1);
    EXPECT_EQ(digits[1], 2); 
    EXPECT_EQ(digits[2], 4); 
}

int main()
{
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
