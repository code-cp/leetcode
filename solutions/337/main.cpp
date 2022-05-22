/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Wed Nov 24 13:11:02 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <gtest/gtest.h> 
#include <memory> 
#include <unordered_map>

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
private:
    unordered_map<shared_ptr<TreeNode<T>>, T> umap;
public:
    int rob(shared_ptr<TreeNode<T>> root) {
        if (root == nullptr) return 0;
        if (root->left == nullptr && root->right == nullptr) return root->val;

        if (umap[root]) return umap[root];

        int val1 = root->val;
        if (root->left) val1 += rob(root->left->left) + rob(root->left->right);
        if (root->right) val1 += rob(root->right->left) + rob(root->right->right);

        int val2 = rob(root->left) + rob(root->right);
        umap[root] = max(val1, val2);
        return max(val1, val2);
    }
};

TEST(Test337, SimpleTest) {
    auto root = make_shared<TreeNode<int>>(3);
    auto left1 = make_shared<TreeNode<int>>(2);
    auto right1 = make_shared<TreeNode<int>>(3);
    root->left = left1; 
    root->right = right1; 
    auto right2 = make_shared<TreeNode<int>>(3);
    auto right3 = make_shared<TreeNode<int>>(1);
    left1->right = right2; 
    right1->right = right3;

    Solution<int> s; 
    EXPECT_EQ(s.rob(root), 7);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
