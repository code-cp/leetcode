#include <gtest/gtest.h> 

using namespace std;

class MyLinkedList {
public:
    /** Initialize your data structure here. */
    struct ListNode {
        int val; 
        ListNode* next; 
        ListNode(int x) : val(x), next(nullptr) {}
    };

    MyLinkedList() {
        _dummyHead = new ListNode(0); 
        _size = 0; 
    }
    
    /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    int get(int index) {
        if (index > (_size - 1) || index < 0) {
            return -1; 
        }
        ListNode* cur = _dummyHead->next; 
        while (index--) {
            cur = cur->next; 
        }
        return cur->val; 
    }
    
    /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
    void addAtHead(int val) {
        ListNode* newNode = new ListNode(val); 
        newNode->next = _dummyHead->next; 
        _dummyHead->next = newNode; 
        _size++; 
    }
    
    /** Append a node of value val to the last element of the linked list. */
    void addAtTail(int val) {
        ListNode* cur = _dummyHead; 
        while (cur->next != nullptr) {
            cur = cur->next; 
        }
        ListNode* newNode = new ListNode(val);
        cur->next = newNode; 
        _size++; 
    }
    
    /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
    void addAtIndex(int index, int val) {
        if (index > _size)
            return; 
        ListNode* newNode = new ListNode(val);
        ListNode* cur = _dummyHead; 
        while (index--) {
            cur = cur->next; 
        }
        newNode->next = cur->next; 
        cur->next = newNode; 
        _size++; 
    }
    
    /** Delete the index-th node in the linked list, if the index is valid. */
    void deleteAtIndex(int index) {
        if (index < 0 || index > _size - 1)
            return; 
        ListNode* cur = _dummyHead; 
        while (index--) {
            cur = cur->next; 
        }
        ListNode* tmp = cur->next; 
        cur->next = tmp->next; 
        delete tmp; 
        _size--; 
    }
private: 
    ListNode* _dummyHead; 
    int _size; 
};

TEST(Test707, SimpleTest)
{
    int result;

    MyLinkedList myLinkedList = MyLinkedList();
    myLinkedList.addAtHead(1);
    myLinkedList.addAtTail(3);
    myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
    result = myLinkedList.get(1);              // return 2
    EXPECT_EQ(result, 2); 
    myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
    result = myLinkedList.get(1);              // return 3
    EXPECT_EQ(result, 3); 
}

int main() {
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS(); 
}
