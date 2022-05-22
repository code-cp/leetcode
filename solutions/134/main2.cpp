#include <iostream>
#include <numeric>
#include <algorithm> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
private:
    // use dynamic programming to find max subarray sum in circular array 
    int maxSub(const vector<int>& vec)
    {
        // check input 
        if (vec.size() == 1 && vec[0] < 0)
            return -1; 
        else if (vec.size() == 1 && vec[0] >= 0)
            return 0; 

        // check total sum 
        int total = accumulate(vec.begin(), vec.end(), 0); 
        if (total < 0)
            return -1; 

        int max_so_far = vec[0], cur_max = vec[0]; 
        int min_so_far = vec[0], cur_min = vec[0];
        int max_id = 0, MAX_id = 0, min_id = 0; 
        int result_sum, result_id; 

        for (int i = 1; i < vec.size(); ++i)
        {
            if (cur_max < 0)
            {
                cur_max = vec[i]; 
                max_id = i; 
            }
            else 
            {
                cur_max += vec[i]; 
            }
            if (cur_max > max_so_far)
            {
                max_so_far = cur_max; 
                MAX_id = max_id; 
            }

            if (cur_min > 0)
            {
                cur_min = vec[i]; 
            }
            else 
            {
                cur_min += vec[i]; 
            }
            if (cur_min < min_so_far)
            {
                min_so_far = cur_min;
                min_id = i; 
            }
        }

        if (max_so_far > (total - min_so_far))
        {
            result_id = MAX_id; 
        }
        else 
        {
            result_id = (min_id + 1) % vec.size(); 
        }

        return result_id; 
    }
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        transform(gas.begin(), gas.end(), cost.begin(), gas.begin(), minus<int>());
        return maxSub(gas); 
    }
};

TEST(Test134, SimpleTest)
{
    vector<int> gas = {1,2,3,4,5};
    vector<int> cost = {3,4,5,1,2};
    Solution s; 
    EXPECT_EQ(s.canCompleteCircuit(gas, cost), 3); 
}

int main()
{
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
