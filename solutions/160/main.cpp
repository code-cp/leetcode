#include <gtest/gtest.h> 

using namespace std; 

// Definition for singly-linked list.
struct ListNode {
    int val; 
    ListNode* next; 
    ListNode(int x) : val(x), next(nullptr) {}
}; 

class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode* curA = headA; 
        ListNode* curB = headB; 
        while (curA != curB) {
            curA = curA == nullptr ? headB : curA->next; 
            curB = curB == nullptr ? headA : curB->next; 
        }

        return curA; 
    }
};

TEST(Test160, SimpleTest) {
    ListNode* headA = new ListNode(1);
    ListNode* n1A = new ListNode(9);
    ListNode* n2A = new ListNode(1);
    ListNode* n3A = new ListNode(2);
    ListNode* n4A = new ListNode(4);

    headA->next = n1A; 
    n1A->next = n2A; 
    n2A->next = n3A; 
    n3A->next = n4A; 

    ListNode* headB = new ListNode(3);
    headB->next = n3A; 

    Solution s; 
    ListNode* inter = s.getIntersectionNode(headA, headB);

    EXPECT_EQ(inter, n3A); 

    delete headA;
    delete n1A;  
    delete n2A;
    delete n3A;
    delete n4A;
    delete headB; 
}

int main() {
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS();
}