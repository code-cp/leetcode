#include <queue> 
#include <memory> 
#include <gtest/gtest.h> 

using namespace std; 

class MyStack {
public:
    queue<int> q1; 
    queue<int> q2; 

    MyStack() {

    }
    
    void push(int x) {
        q1.push(x); 
    }
    
    int pop() {
        int qSize = q1.size(); 
        while (qSize-- != 1) {
            q2.push(q1.front());
            q1.pop();  
        }

        int result = q1.front(); 
        q1.pop();
        // copy queue 
        q1 = q2;
        qSize = q2.size();  
        while (qSize--) {
            q2.pop(); 
        }
        return result; 
    }
    
    int top() {
        return q1.back(); 
    }
    
    bool empty() {
        return q1.empty(); 
    }
};

TEST(Test225, SimpleTest) {
    auto myStack = make_unique<MyStack>();
    myStack->push(1); 
    myStack->push(2); 
    EXPECT_EQ(myStack->top(), 2); 
    EXPECT_EQ(myStack->pop(), 2); 
    EXPECT_FALSE(myStack->empty()); 
}

int main() {
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS(); 
}