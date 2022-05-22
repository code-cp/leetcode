#include <gtest/gtest.h> 

using namespace std; 

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
 };
 
// recursive solution 
// each time only reverse a simple block with two nodes 
class Solution {
public:
    ListNode* helper(ListNode* cur, ListNode* pre) {
        // base case 
        if (cur == nullptr) 
            return pre; 
        ListNode* tmp = cur->next; 
        cur->next = pre; 
        return helper(tmp, cur); 
    }
    ListNode* reverseList(ListNode* head) {
        return helper(head, nullptr); 
    }
};

TEST(Test206, SimpleTest) {
    ListNode* head = new ListNode(1); 
    ListNode* n1 = new ListNode(2); 
    ListNode* n2 = new ListNode(3); 
    ListNode* n3 = new ListNode(4);
    ListNode* n4 = new ListNode(5); 

    head->next = n1; 
    n1->next = n2; 
    n2->next = n3; 
    n3->next = n4; 
    
    Solution s; 
    ListNode* sol = s.reverseList(head); 

    ListNode* cur = sol; 
    int count = 5; 
    while (cur != nullptr) {
        EXPECT_EQ(cur->val, count);
        count--; 
        cur = cur->next; 
    }

    delete head;
    delete n1;
    delete n2;
    delete n3;
    delete n4; 
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS(); 
}