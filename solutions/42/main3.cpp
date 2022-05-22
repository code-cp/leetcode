#include <iostream> 
#include <stack>
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int trap(vector<int>& height) {
        
        const int n = height.size(); 
        stack<pair<int, int>> s; 
        int water = 0; 

        for (int i = 0; i < n; ++i)
        {
            int temp_height = 0; 

            // deal with the lower bar or bar with equal height 
            while (!s.empty())
            {
                int bar = s.top().first; 
                int pos = s.top().second;

                // calculate the water trapped by the bar, temp_height, height[i]
                water += (min(bar, height[i]) - temp_height) * (i - pos - 1); 
                temp_height = bar; 

                // if bar in stack is higher than current height, exit 
                // else, pop the stack 
                if (height[i] < bar)
                    break;
                else 
                    s.pop();  
            }

            s.push(make_pair(height[i], i)); 
        }

        return water; 
    }
};

TEST(Test42, SimpleTest)
{
    vector<int> height = {0,1,0,2,1,0,1,3,2,1,2,1}; 
    Solution s; 
    EXPECT_EQ(s.trap(height), 6) << "wrong answer"; 
}

int main() 
{
   testing::InitGoogleTest();
   return RUN_ALL_TESTS();
}
