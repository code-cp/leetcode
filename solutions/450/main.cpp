/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Fri Oct 29 10:47:33 2021
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
class Solution {
public:
    shared_ptr<TreeNode<T>> deleteNode(shared_ptr<TreeNode<T>> root, T key) {
        // key is not found 
        if (root == nullptr) return root; 
        if (root->val == key) {
            // both left, right are empty, return null 
            // left is empty, right is not, return right 
            if (root->left == nullptr) return root->right; 
            // right is null, left is not, return left 
            else if (root->right == nullptr) return root->left; 
            else {
                // both children non empty, more complicated 
                // put left to be under the leftmost child of right tree 
                auto cur = root->right; 
                // find leftmost child of right tree  
                while (cur->left != nullptr) cur = cur->left; 
                cur->left = root->left; 
                root = root->right; 
                return root; 
            }
        }
        if (root->val > key) root->left = deleteNode(root->left, key); 
        if (root->val < key) root->right = deleteNode(root->right, key); 
        return root; 
    }
};

TEST(Test450, SimpleTest) {
    auto root = make_shared<TreeNode<int>>(1);
    auto left = make_shared<TreeNode<int>>(0);
    auto right = make_shared<TreeNode<int>>(2);
    root->left = left; 
    root->right = right; 

    const int key = 2;

    Solution<int> s; 
    auto root1 = s.deleteNode(root, key);
    EXPECT_FALSE(root->right);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
