// note there is already a partition function in C++ https://codereview.stackexchange.com/a/88503
template<class RandomIt, class Compare> RandomIt myPartition(RandomIt first, RandomIt end, Compare cmp) {
    // choose the last element as pivot 
    // O(n) average case complexity
    auto last = next(end, -1); 
    auto pivot = *last; 

    while (first < last) {
        while (cmp(*first, pivot)) ++first; 
        while (cmp(pivot, *last)) --last; 
        if (first < last) { 
            swap(*first, *last); 
            // to deal with equal values 
            if (*first == *last) --last; 
        }
    }

    return first; 
}

// input: 9, 3, 6, 2, 1, 7, 8, 5, 4, 0
// std::nth_element(v.begin(), v.begin() + 2, v.end());
// output: 1 0 2 3 6 7 8 5 4 9 
// 0 1 2 3 4 5 6 7 8 9 
//     ^--- begin() + 2
template<class RandomIt, class Compare> void quickSelect(RandomIt first, RandomIt end, int k, Compare cmp) {
    auto p = myPartition(first, end, cmp); 
    if (p-first+1 == k) return; 
    if (p-first+1 < k) quickSelect(p+1, end, k-(p-first+1), cmp); 
    else quickSelect(first, p, k, cmp); 
}

class Solution {
public: 
    // N (1 + 1/2 + 1/4 + …) = O(N)
    double trimMean(vector<int>& arr) {
        int pos = arr.size() * 0.05; 
        quickSelect(arr.begin(), arr.end(), pos, [](int &a, int &b){
            return a<b;
        }); 
        quickSelect(arr.rbegin(), arr.rend(), pos, [](int &a, int &b){
            return a>b;
        }); 
        return accumulate(arr.begin() + pos, arr.end() - pos, 0.0) / (arr.size() * 0.9); 
    }
}; 