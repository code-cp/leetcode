#include <gtest/gtest.h>

using namespace std; 

// Definition for singly-linked list
struct ListNode {
    int val; 
    ListNode* next; 
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {} 
};

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummyHead = new ListNode(0, head); 
        ListNode* fast = dummyHead; 
        ListNode* slow = dummyHead; 

        while (n-- && fast->next != nullptr) {
            fast = fast->next; 
        }

        while (fast->next != nullptr) {
            fast = fast->next; 
            slow = slow->next; 
        }

        slow->next = slow->next->next; 

        return dummyHead->next; 
    }
};

TEST(Test19, SimpleTest) {
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
    ListNode* sol = s.removeNthFromEnd(head, 2); 

    EXPECT_EQ(sol->val, 1);  
    EXPECT_EQ(sol->next->val, 2); 
    EXPECT_EQ(sol->next->next->val, 3); 
    EXPECT_EQ(sol->next->next->next->val, 5);

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