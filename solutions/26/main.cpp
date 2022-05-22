#include <iostream>
#include <vector>
#include <gtest/gtest.h>

using namespace std; 

class Solution {
public: 
   int removeDuplicates(vector<int>& nums) {
       // check input 
       if (nums.empty()) 
           return 0; 
       
       int index = 0; 
       for (int i = 1; i < nums.size(); ++i)
       {
           if (nums[i] != nums[index])
           {
               ++index; 
               nums[index] = nums[i]; 
           }
       }
       
       return index + 1; 
   } 
};

TEST(Test26, SimpleTest) 
{
    vector<int> nums = {1, 1, 2}; 
    Solution s; 
    int index = s.removeDuplicates(nums); 
    EXPECT_EQ(index, 2) << "incorrect index"; 
}

int main() 
{
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
