/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Wed Oct 27 10:52:11 2021
> Description:   
 ************************************************************************/
#include <vector>
#include <algorithm> 
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
class RecusriveSolution {
public:
    shared_ptr<TreeNode<T>> lowestCommonAncestor(shared_ptr<TreeNode<T>> root, shared_ptr<TreeNode<T>> p, shared_ptr<TreeNode<T>> q) {
        if (root == nullptr) return nullptr; 

        // post order traversal, left, right, visit 
        if (p->val > q->val) {
            shared_ptr<TreeNode<T>> temp = p; 
            p = q; 
            q = temp; 
        } 
        
        if (root->val > q->val) 
            return lowestCommonAncestor(root->left, p, q);
        else if (root->val < p->val) 
            return lowestCommonAncestor(root->right, p, q); 
        else 
            return root; 
    }
};

template <typename T>
class IterativeSolution {
public:
    shared_ptr<TreeNode<T>> lowestCommonAncestor(shared_ptr<TreeNode<T>> root, shared_ptr<TreeNode<T>> p, shared_ptr<TreeNode<T>> q) {
        if (p->val > q->val) {
            shared_ptr<TreeNode<T>> temp = p;
            p = q;
            q = temp;
        }
        while (root != nullptr) {
            if (root->val > q->val) root = root->left;
            else if (root->val < p->val) root = root->right;
            else return root;
        }
        return nullptr;
    }
};

TEST(Test235, SimpleTest) {
    auto root = make_shared<TreeNode<int>>(2);
    auto left = make_shared<TreeNode<int>>(1);
    root->left = left; 
    
    RecusriveSolution<int> rs;
    EXPECT_EQ(rs.lowestCommonAncestor(root, root, left)->val, 2);
    IterativeSolution<int> is;
    EXPECT_EQ(is.lowestCommonAncestor(root, root, left)->val, 2);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
