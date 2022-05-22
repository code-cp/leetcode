#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    void reverseString(vector<char>& s) {
        for (int i = 0, j = s.size() - 1; i < s.size() / 2; ++i, --j) {
            swap(s[i], s[j]);
        }
    }
};

TEST(Test344, SimpleTest) {
    vector<char> input_vec = {'h', 'e', 'l', 'l', 'o'}; 
    vector<char> output_vec = {'o', 'l', 'l', 'e', 'h'}; 
    Solution s; 
    s.reverseString(input_vec); 
    for (int i = 0; i < input_vec.size(); ++i) {
        EXPECT_EQ(input_vec[i], output_vec[i]);
    }
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS(); 
}