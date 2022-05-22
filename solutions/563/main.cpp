/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Wed Nov 17 16:20:53 2021
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
    int dfs(shared_ptr<TreeNode<T>> root, int& tiltSum) {
        // base case
        if (root == nullptr) return 0;

        // post order traversal
        int leftSum = dfs(root->left, tiltSum);
        int rightSum = dfs(root->right, tiltSum);
        int totalSum = leftSum + rightSum + root->val;
        root->val = totalSum;
        tiltSum += abs(leftSum - rightSum);
        return totalSum;
    }
    int findTilt(shared_ptr<TreeNode<T>> root) {
        int tiltSum = 0;
        dfs(root, tiltSum);
        return tiltSum;
    }
};

TEST(Test563, SimpleTest) {
    auto root = make_shared<TreeNode<int>>(1);
    auto left = make_shared<TreeNode<int>>(2);
    auto right = make_shared<TreeNode<int>>(3);
    root->left = left; 
    root->right = right; 
    Solution<int> s; 
    EXPECT_EQ(s.findTilt(root), 1);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
