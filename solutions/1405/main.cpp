#include <queue> 
#include <string> 
#include <gtest/gtest.h> 

using namespace std; 

typedef pair<int, string> pis; 

class Solution {
public:
    string longestDiverseString(int a, int b, int c) {
        string result = ""; 
        priority_queue<pis> pq; 
        if (a > 0) pq.push({a, "a"});
        if (b > 0) pq.push({b, "b"});
        if (c > 0) pq.push({c, "c"});
        int max_count = 0; 
        string pre_alph, new_alph; 
        while (true) {
            pis max_alph = pq.top();
            if (max_alph.first == 0) return result;  
            pq.pop(); 
            result += max_alph.second; 
            pre_alph = max_alph.second; 
            max_alph.first--; 
            pq.push(max_alph); 
            max_count++; 

            if (max_count == 2) {
                pis max_alph = pq.top(); 
         
                if (max_alph.second != pre_alph)
                {
                    if (max_alph.first == 0) return result;
                    pq.pop(); 
                    new_alph = max_alph.second; 
                    max_alph.first--; 
                    pq.push(max_alph);
                }
                else if (pq.size() == 1) return result; 
                else {
                    pq.pop(); 
                    pis sec_alph = pq.top();
                    if (sec_alph.first == 0) return result;
                    pq.pop();
                    new_alph = sec_alph.second; 
                    sec_alph.first--;
                    pq.push(sec_alph);
                    pq.push(max_alph);
                }

                result += new_alph; 
                max_count = 0; 
            }
        } 
        return result; 
    }
};

TEST(Test1405, SimpleTest) {
    int a = 1, b = 1, c = 7; 
    string ans = "ccaccbcc";
    Solution s; 
    EXPECT_EQ(s.longestDiverseString(a, b, c).size(), ans.size()); 
}

int main() {
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS(); 
}