class Solution {
public: 
    double trimMean(vector<int>& arr) {
        int pos = arr.size() * 0.05; 
        // ref https://stackoverflow.com/a/69230670/8519188
        // ref https://stackoverflow.com/questions/29145520/how-is-nth-element-implemented
        nth_element(arr.begin(), arr.begin() + pos, arr.end()); 
        nth_element(arr.rbegin(), arr.rbegin() + pos, arr.rend(), greater{}); 
        return accumulate(arr.begin() + pos, arr.end() - pos, 0.0) / (arr.size() * 0.9); 
    }
}; 