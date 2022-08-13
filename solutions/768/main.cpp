class Solution {
public: 
    int maxChunksToSorted(vector<int>& arr) {
        auto exp = arr; 
        sort(exp.begin(), exp.end());

        // NOTE, int has overflow 
        long long int sum1 = 0, sum2 = 0, count = 0; 
        for (int i = 0; i < arr.size(); ++i) {
            sum1 += arr[i]; 
            sum2 += exp[i]; 

            if (sum1 == sum2) {
                count++; 
                sum1 = 0; 
                sum2 = 0;
            }
        }
        return count; 
    }
};