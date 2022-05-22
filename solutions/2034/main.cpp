/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sun Jan 23 08:47:42 2022
> Description:   
 ************************************************************************/
#include <iostream> 
#include <queue> 
#include <unordered_map> 
#include <gtest/gtest.h> 

using namespace std; 

typedef pair<int, int> pii; 

class StockPrice {
private: 
    int _max_timestamp; 
    unordered_map<int, int> _time_price_map; 
    priority_queue<pii, vector<pii>, less<pii>> _pq_max; 
    priority_queue<pii, vector<pii>, greater<pii>> _pq_min; 
public:
    StockPrice(): _max_timestamp(0) {}
    
    void update(int timestamp, int price) {
        _max_timestamp = max(_max_timestamp, timestamp); 
        _time_price_map[timestamp] = price; 
        _pq_max.emplace(price, timestamp); 
        _pq_min.emplace(price, timestamp); 
    }
    
    int current() {
        return _time_price_map[_max_timestamp]; 
    }
    
    int maximum() {
        while (true) {
            int price = _pq_max.top().first, timestamp = _pq_max.top().second; 
            if (_time_price_map[timestamp] == price) return price; 
            _pq_max.pop(); 
        }
    }
    
    int minimum() {
        while (true) {
            int price = _pq_min.top().first, timestamp = _pq_min.top().second; 
            if (_time_price_map[timestamp] == price) return price; 
            _pq_min.pop(); 
        }
    }
};

TEST(Test2034, SimpleTest) {
    StockPrice stockPrice;
    stockPrice.update(1, 10);
    stockPrice.update(2, 5);
    cout << stockPrice.current() << endl; 
    cout << stockPrice.maximum() << endl; 
    stockPrice.update(1, 3);
    cout << stockPrice.maximum() << endl; 
    stockPrice.update(4, 2);
    cout << stockPrice.minimum() << endl;
}
