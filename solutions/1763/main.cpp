#include <string> 
#include <unordered_map>
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
private: 
    unordered_map<char, int> _umap; 
    int _max_pos;
    int _max_len;  
    char matchChar(const char& c) {
        if (c >= 'a' && c <= 'z') return c-('a'-'A');
        else return c+('a'-'A');
    }
public:
    Solution() : _max_pos(0), _max_len(0) {} 
    void helper(const string& s, int k) {
        int r = 0; 
        int unique_match_char_num = 0;
        char match; 
        _umap.clear(); 

        for (int l = 0; l < s.size(); ++l) {

            if (_umap.size() == k && unique_match_char_num*2 == k) {
                if (r-l > _max_len) {
                    _max_pos = l; 
                    _max_len = r-l;
                }
            }

            while (r < s.size() && _umap.size() <= k) {
                _umap[s[r]]++; 
                match = matchChar(s[r]); 
                if (_umap[s[r]] == 1 && _umap.count(match) > 0) unique_match_char_num++; 

                if (_umap.size() == k && unique_match_char_num*2 == k) {
                    if (r-l+1 > _max_len) {
                        _max_pos = l; 
                        _max_len = r-l+1;
                    }
                }

                r++;
            } 

            _umap[s[l]]--;
            if (_umap[s[l]] == 0) {
                match = matchChar(s[l]);
                if (_umap.count(match) > 0) {
                    unique_match_char_num -= 1;
                }
                _umap.erase(s[l]);
            } 
        }
    }
    string longestNiceSubstring(string s) {
        for (int k = 2; k <= 52; k+=2) helper(s, k); 
        return s.substr(_max_pos, _max_len); 
    }
};

TEST(Test1763, SimpleTest) {
    string s = "YazaAay"; 
    Solution sol; 
    EXPECT_EQ(sol.longestNiceSubstring(s), "aAa"); 
}

int main() {
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS(); 
}
