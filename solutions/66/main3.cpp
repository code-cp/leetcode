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
        
        // use lambda expression 
        for_each(digits.rbegin(), digits.rend(), 
            [&carry](auto & d){
                d += carry; 
                carry = d / 10; 
                d %= 10; 
            }
        );

        if (carry > 0)
            digits.insert(digits.begin(), carry); 
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
