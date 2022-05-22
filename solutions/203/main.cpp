// for smart pointer 
#include <memory> 
#include <gtest/gtest.h>

using namespace std; 

struct ListNode {
    int val; 
    shared_ptr<ListNode> next; 
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {} 
    ListNode(int x, const shared_ptr<ListNode>& next) : val(x), next(next) {} 
};

class Solution {
public:
    auto removeElements(const shared_ptr<ListNode>& head, int val) {
        auto dummyHead = make_shared<ListNode>(0, head); 
        auto cur = dummyHead; 
        while (cur->next != nullptr) {
            if (cur->next->val == val)
                cur->next = cur->next->next;
            else 
                cur = cur->next; 
        } 
        return dummyHead->next; 
    }
};

TEST(Test203, SimpleTest)
{
    const int val = 6; 

    auto ans{make_shared<ListNode>(1)};
    auto n1a{make_unique<ListNode>(2)};
    auto n2a{make_unique<ListNode>(3)};
    auto n3a{make_unique<ListNode>(4)};
    auto n4a{make_unique<ListNode>(5)};

    n3a->next = move(n4a);
    n2a->next = move(n3a); 
    n1a->next = move(n2a);   
    ans->next = move(n1a); 

    auto input{make_shared<ListNode>(1)};
    auto n1i{make_unique<ListNode>(2)};
    auto n2i{make_unique<ListNode>(6)};
    auto n3i{make_unique<ListNode>(3)};
    auto n4i{make_unique<ListNode>(4)};
    auto n5i{make_unique<ListNode>(5)};
    auto n6i{make_unique<ListNode>(6)};

    n5i->next = move(n6i); 
    n4i->next = move(n5i);
    n3i->next = move(n4i);
    n2i->next = move(n3i); 
    n1i->next = move(n2i); 
    input->next = move(n1i); 

    Solution s; 
    auto sol = s.removeElements(input, val); 

    auto cur_ans{make_shared<ListNode>(0)};
    cur_ans->next = ans; 

    auto cur_sol{make_shared<ListNode>(0)};
    cur_sol->next = sol; 

    while (cur_ans->next != nullptr) {
        EXPECT_EQ(cur_ans->val, cur_sol->val); 
        cur_ans = cur_ans->next; 
        cur_sol = cur_sol->next; 
    }
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS(); 
}