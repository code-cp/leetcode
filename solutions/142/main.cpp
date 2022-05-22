#include <gtest/gtest.h> 

using namespace std; 

// Definition for singly-linked list.
struct ListNode {
    int val; 
    ListNode* next; 
    ListNode(int x) : val(x), next(nullptr) {}
}; 

// time complexity O(m+n)
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB, ListNode *pseudoEnd) {
        ListNode* curA = headA; 
        ListNode* curB = headB; 
        while (curA != curB) {
            curA = curA == pseudoEnd ? headB : curA->next; 
            curB = curB == pseudoEnd ? headA : curB->next; 
        }

        return curA; 
    }

    ListNode *detectCycle(ListNode *head) {
        ListNode* fast = head; 
        ListNode* slow = head; 
        while (fast != nullptr && fast->next != nullptr && fast->next != slow) {
            fast = fast->next->next; 
            slow = slow->next; 
        }
        if (fast == nullptr || fast->next == nullptr)
            return nullptr; 
        else {
            ListNode* pseudoEnd = fast;
            return getIntersectionNode(head, slow, pseudoEnd); 
        }
    }
};

TEST(Test142, SimpleTest) {
    ListNode* headA = new ListNode(3);
    ListNode* n1A = new ListNode(2);
    ListNode* n2A = new ListNode(0);
    ListNode* n3A = new ListNode(-4);

    headA->next = n1A; 
    n1A->next = n2A; 
    n2A->next = n3A; 
    n3A->next = n1A; 

    Solution s; 
    ListNode* inter = s.detectCycle(headA);

    EXPECT_EQ(inter, n1A); 

    delete headA;
    delete n1A;  
    delete n2A;
    delete n3A;
}

int main() {
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS();
}