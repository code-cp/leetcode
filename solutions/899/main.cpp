#include <string> 

class Solution {
public: 
    string orderlyQueue(string s, int k) {
        int n = s.size(); 
        if (k == 1) {
            string ans = s; 
            for (int i = 1; i < n; i++) {
                string t = s.substr(i) + s.substr(0, i); 
                if (ans > t) ans = t; 
            }
            return ans; 
        }
        sort(s.begin(), s.end());
        return s;
    }
};