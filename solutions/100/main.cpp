/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Fri Oct 15 09:36:29 2021
> Description:   
 ************************************************************************/
#include <memory> 
#include <gtest/gtest.h> 

using namespace std; 

template <typename T> 
struct TreeNode {
    T val; 
    shared_ptr<TreeNode<T>> left;
    shared_ptr<TreeNode<T>> right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {

    }
    TreeNode(T x) : val(x), left(nullptr), right(nullptr) {

    }
    TreeNode(T x, shared_ptr<TreeNode<T>> left, shared_ptr<TreeNode<T>> right) : val(x), left(left), right(right) {

    }
};

template <typename T> 
class RecursiveSolution {
public:
    bool isSameTree(shared_ptr<TreeNode<T>> p, shared_ptr<TreeNode<T>> q) {
        if (p == nullptr && q != nullptr) return false;
        if (p != nullptr && q == nullptr) return false;
        if (p == nullptr && q == nullptr) return true;
        // pre order traversal, visit, left, right
        if (p->val != q->val) return false;
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};

class IterativeSolution {
public:
    bool isSameTree(shared_ptr<TreeNode<T>> p, shared_ptr<TreeNode<T>> q) {
        if (p == nullptr && q == nullptr) return true;
        if (p == nullptr || q == nullptr) return false;
        queue<shared_ptr<TreeNode<T>>> mq;
        mq.push(p);
        mq.push(q);
        while (!mq.empty()) {
            for (int i = 0; i < mq.size(); i+=2) {
                shared_ptr<TreeNode<T>> node1 = mq.front();
                mq.pop();
                shared_ptr<TreeNode<T>> node2 = mq.front();
                mq.pop();
                if (node1 == nullptr && node2 == nullptr) continue;
                if (node1 == nullptr || node2 == nullptr) return false;
                if (node1->val != node2->val) return false;
                mq.push(node1->left);
                mq.push(node2->left);
                mq.push(node1->right);
                mq.push(node2->right);
            }
        }
        return true;
    }
};

TEST(Test100, SimpleTest) {
    auto root1 = make_shared<TreeNode<int>>(1);
    auto node1 = make_shared<TreeNode<int>>(2);
    auto node2 = make_shared<TreeNode<int>>(3);
    root1->left = node1; 
    root1->right = node2; 

    auto root2 = make_shared<TreeNode<int>>(1);
    auto node3 = make_shared<TreeNode<int>>(2);
    auto node4 = make_shared<TreeNode<int>>(3);
    root2->left = node3;
    root2->right = node4;

    IterativeSolution<int> is; 
    EXPECT_TRUE(is.isSameTree(root1, root2));
    RecursiveSolution<int> rs;
    EXPECT_TRUE(rs.isSameTree(root1, root2));
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
