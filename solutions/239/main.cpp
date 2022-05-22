#include <deque> 
#include <vector>
#include <gtest/gtest.h> 

using namespace std; 

// always keep the largest number and the 
// second largest number in window in the queue 
// when largest number poped out, the second largest becomes 
// the largest 
// time complexity O(n)
// space complexity O(k)
class Solution {
public:
    class MyQueue {
    public: 
        deque<int> que; 
        void pop(int value) {
            if (!que.empty() && value == que.front()) {
                que.pop_front(); 
            }
        }
        void push(int value) {
            while (!que.empty() && value > que.back()) {
                que.pop_back(); 
            }
            que.push_back(value); 
        }
        int front() {
            return que.front(); 
        }
    };
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        MyQueue que; 
        vector<int> result; 
        for (int i = 0; i < k; ++i) {
            que.push(nums[i]); 
        }
        result.push_back(que.front());
        for (int i = k; i < nums.size(); ++i) {
            que.pop(nums[i - k]);
            que.push(nums[i]); 
            result.push_back(que.front());
        }
        return result; 
    }
};

TEST(Test239, SimpleTest) {
    vector<int> nums = {1,3,-1,-3,5,3,6,7}; 
    const int k = 3; 
    vector<int> ans = {3,3,5,5,6,7};
    Solution s; 
    vector<int> result = s.maxSlidingWindow(nums, k); 
    for (int i = 0; i < ans.size(); ++i) {
        EXPECT_EQ(ans[i], result[i]); 
    }
}

int main() {
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS(); 
}