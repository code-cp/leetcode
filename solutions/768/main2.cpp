class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        stack<int> st; 
        int curMax = 0; 
        for (auto a: arr) {
            if (st.empty() || st.top() <= a) {
                st.push(a); 
                curMax = a; 
            }
            else {
                while (!st.empty() && st.top() > a) st.pop(); 
                st.push(curMax); 
            }
        }
        return st.size(); 
    }
};