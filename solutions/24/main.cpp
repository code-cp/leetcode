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

class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        // note we use dummy head node so that 
        // we do not have to deal with head node separately 
        ListNode* dummyHead = new ListNode(0, head); 
        ListNode* cur = dummyHead; 
        while (cur->next != nullptr && cur->next->next != nullptr) {
            ListNode* tmp1 = cur->next; 
            ListNode* tmp2 = tmp1->next; 

            cur->next->next = tmp2->next; 
            tmp2->next = cur->next; 
            cur->next = tmp2; 
            cur = tmp1; 
        }
        return dummyHead->next; 
    }
};

TEST(Test24, SimpleTest) {
    ListNode *head = new ListNode(1); 
    ListNode *n1 = new ListNode(2); 
    ListNode *n2 = new ListNode(3); 
    ListNode *n3 = new ListNode(4); 

    head->next = n1; 
    n1->next = n2; 
    n2->next = n3; 

    Solution s; 
    ListNode *sol = s.swapPairs(head); 

    EXPECT_EQ(sol->val, 2); 
    EXPECT_EQ(sol->next->val, 1); 
    EXPECT_EQ(sol->next->next->val, 4); 
    EXPECT_EQ(sol->next->next->next->val, 3);

    delete head; 
    delete n1; 
    delete n2; 
    delete n3;  
}

int main() {
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS(); 
}

