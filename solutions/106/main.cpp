/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sun Oct 17 13:24:27 2021
> Description:   
 ************************************************************************/
#include <memory>
#include <vector>
#include <iostream> 
#include <gtest/gtest.h> 

using namespace std; 

template <typename T> 
struct TreeNode {
    T val; 
    shared_ptr<TreeNode<T>> left; 
    shared_ptr<TreeNode<T>> right; 
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(T x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(T x, shared_ptr<TreeNode<T>> left, shared_ptr<TreeNode<T>> right) :
        val(x), left(left), right(right) {} 
};

template <typename T>
class Solution {
public:
    shared_ptr<TreeNode<T>> buildTree(vector<T>& inorder, vector<T>& postorder) {
        if (postorder.size() == 0) return nullptr;

        T rootValue = *(postorder.end() - 1);
        auto root = make_shared<TreeNode<T>>(rootValue);
        if (postorder.size() == 1) return root;

        auto delimiterIt = find(inorder.begin(), inorder.end(), rootValue);
        // [0, delimiterIndex)
        vector<T> leftInorder(inorder.begin(), delimiterIt);
        // [delimiterIndex + 1, end)
        vector<T> rightInorder(delimiterIt + 1, inorder.end());

        postorder.resize(postorder.size() - 1);
        // [0, leftInorder.size)
        vector<T> leftPostorder(postorder.begin(), postorder.begin() + leftInorder.size());
        // [leftInorder.size, end)
        vector<T> rightPostorder(postorder.begin() + leftInorder.size(), postorder.end());

        root->left = buildTree(leftInorder, leftPostorder);
        root->right = buildTree(rightInorder, rightPostorder);

        return root;
    }
};

TEST(Test106, SimpleTest) {
    vector<int> inorder = {
        9,3,15,20,7
    };
    vector<int> postorder = {
        9,15,7,20,3
    };
    Solution<int> s;
    auto root = s.buildTree(inorder, postorder);
    EXPECT_EQ(root->val, 3);
    EXPECT_EQ(root->left->val, 9);
    EXPECT_EQ(root->right->val, 20);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
