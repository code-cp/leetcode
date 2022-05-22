/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sun Jan 16 09:35:20 2022
> Description:   
 ************************************************************************/
#include <iostream> 
#include <memory> 
#include <stdlib.h>
#include <gtest/gtest.h> 

using namespace std; 

// Definition for singly-linked list.
template <typename T> 
struct ListNode {
    T val;
    shared_ptr<ListNode<T>> next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(T x) : val(x), next(nullptr) {}
    ListNode(T x, shared_ptr<ListNode<T>> next) : val(x), next(next) {}
};

template <typename T> 
class Solution {
private:
    shared_ptr<ListNode<T>> _head;
public:
    Solution(shared_ptr<ListNode<T>> head) {
        _head = head;
        srand(0);
    }
    int getRandom() {
        shared_ptr<ListNode<T>> cur = _head;
        int result = cur->val;
        int count = 0;
        while (cur != nullptr) {
            count++;
            if (rand() % count == 1) result = cur->val;
            cur = cur->next;
        }
        return result;
    }
};

TEST(Test382, SimpleTest) {
    auto head = make_shared<ListNode<int>>(0);
    head->next = make_shared<ListNode<int>>(1);

    Solution<int> s(head); 
    cout << "random number: " << s.getRandom() << endl;
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}

