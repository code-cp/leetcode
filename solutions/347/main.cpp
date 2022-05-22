#include <unordered_map>
#include <queue> 
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

// time complexity O(nlogk)
// space complexity O(k)
class Solution {
    // if the element is in the form of pairs, then by default the priority 
    // of the elements is dependent upon the first element
    // min heap, sort by second element 
    class MyCmp {
    public: 
        bool operator()(const pair<int, int>& lhs, const pair<int, int>& rhs) {
            // perhaps queue start is at the end, so use > here
            return lhs.second > rhs.second; 
        }
    };
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> map; 
        for (const auto& n : nums) {
            map[n]++; 
        }

        // sort by frequency 
        priority_queue<pair<int, int>, vector<pair<int, int>>, MyCmp> pq; 
        for (const auto& it : map) {
            pq.push(it); 
            if (pq.size() > k) 
                pq.pop(); 
        }

        // in min heap to return frequency from high 
        // to low, we need to reverse the order 
        vector<int> result(k); 
        for (int i = k - 1; i >= 0; --i) {
            result[i] = pq.top().first; 
            pq.pop(); 
        }
        return result;  
    }
};

TEST(Test347, SimpleTest) {
    vector<int> nums = {1,1,1,2,2,3}; 
    const int k = 2; 
    Solution s; 
    vector<int> result = s.topKFrequent(nums, k);
    EXPECT_EQ(result[0], 1); 
    EXPECT_EQ(result[1], 2); 
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS(); 
}