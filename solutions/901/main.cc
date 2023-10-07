#include <stack> 
using namespace std; 

class StockSpanner {
    stack<int> cnt_stack_; 
    stack<int> num_stack_; 
public:
    StockSpanner() {

    }
    
    int next(int price) {
        if (cnt_stack_.empty()) {
            cnt_stack_.push(1); 
            num_stack_.push(price); 
            return 1; 
        }

        // add today's count 
        int res = 1; 
        while (!num_stack_.empty() && price >= num_stack_.top()) {
            res += cnt_stack_.top(); 
            cnt_stack_.pop(); 
            num_stack_.pop(); 
        }
        cnt_stack_.push(res); 
        num_stack_.push(price);

        return res; 
    }
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */