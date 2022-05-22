#include <stack> 
#include <memory> 
#include <gtest/gtest.h> 

using namespace std; 

class MyQueue {
public:
    stack<int> inStack; 
    stack<int> outStack; 

    MyQueue() {

    }
    
    void push(int x) {
        inStack.push(x); 
    }
    
    int pop() {
        if (outStack.empty()) {
            while (!inStack.empty()) {
                outStack.push(inStack.top());
                inStack.pop();
            }
        }
        int result = outStack.top();
        outStack.pop();
        return result; 
    }
    
    int peek() {
        int result = this->pop();
        outStack.push(result); 
        return result; 
    }
    
    bool empty() {
        return inStack.empty() && outStack.empty(); 
    }
};

TEST(Test232, SimpleTest) {
    unique_ptr<MyQueue> myQueue = make_unique<MyQueue>(); 
    myQueue->push(1);
    myQueue->push(2);
    EXPECT_EQ(myQueue->peek(), 1); 
    myQueue->pop();
    EXPECT_FALSE(myQueue->empty());
}

int main() {
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS();
}