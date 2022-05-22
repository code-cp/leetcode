/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sun Oct 17 14:22:44 2021
> Description:   
 ************************************************************************/
#include <vector>
#include <memory> 
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
    shared_ptr<TreeNode<T>> constructMaximumBinaryTree(vector<T>& nums) {
        // base case
        if (nums.size() == 1) {
            auto node = make_shared<TreeNode<T>>(nums[0]);
            return node;
        }

        auto maxIt = max_element(nums.begin(), nums.end());
        auto root = make_shared<TreeNode<T>>(*maxIt);
        if (distance(nums.begin(), maxIt) > 0) {
            vector<T> leftNums(nums.begin(), maxIt);
            root->left = constructMaximumBinaryTree(leftNums);
        }
        if (distance(maxIt, nums.end()) > 1) {
            vector<T> rightNums(maxIt + 1, nums.end());
            root->right = constructMaximumBinaryTree(rightNums);
        }

        return root;
    }
};

TEST(Test654, SimpleTest) {
    vector<int> nums = {
        3, 2, 1
    };
    Solution<int> s;
    auto root = s.constructMaximumBinaryTree(nums);
    EXPECT_EQ(root->val, 3);
    EXPECT_EQ(root->right->val, 2);
    EXPECT_EQ(root->right->right->val, 1);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
