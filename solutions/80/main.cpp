#include <iostream>
#include <vector>
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        
        // check input 
        if (nums.size() < 3)
            return nums.size();
        
        const int max_count = 2;
        int count, index; 
        count = 1; 
        index = 0; 
        for (int i = 1; i < nums.size(); i++)
        {
            if (nums[i] == nums[index])
            {
                if (count >= max_count)
                {
                    count++;  
                }
                else
                {
                    ++count; 
                    ++index; 
                    nums[index] = nums[i];
                }
            }
            else
            {
                count = 1; 
                ++index; 
                nums[index] = nums[i];
            }
        }
        return index + 1; 
    }
};


TEST(Test80, SimpleTest) {
    vector<int> nums = {1,1,1,2,2,3}; 
    Solution s; 
    EXPECT_EQ(s.removeDuplicates(nums), 5) << 
	"wrong answer, expected 5"; 
}

int main() {
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS(); 
} 

