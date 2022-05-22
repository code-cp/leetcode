/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Wed Nov 10 10:23:32 2021
> Description:   
 ************************************************************************/
#include <memory> 
#include <gtest/gtest.h> 

using namespace std; 

struct TreeNode {
    int val; 
    shared_ptr<TreeNode> left; 
    shared_ptr<TreeNode> right; 
    TreeNode() : val(0), left(nullptr), right(nullptr) {

    }
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {

    }
    TreeNode(int x, shared_ptr<TreeNode> left, shared_ptr<TreeNode> right) : val(x), left(left), right(right) {

    }
};

class Solution {
private:
    int result;
public:
    Solution() : result(0) {}
    // state:
    // 0 = not covered
    // 1 = has camera
    // 2 = covered
    int traversal(shared_ptr<TreeNode> cur) {
        // nullptr is covered
        if (cur == nullptr) return 2;

        // post order traversal, left, right, visit
        int left = traversal(cur->left);
        int right = traversal(cur->right);

        // case 1, both children are covered
        if (left == 2 && right == 2) return 0;
        // case 2, one of children is not covered
        if (left == 0 || right == 0) {
            result++;
            return 1;
        }

        // case 2, one of children has camera
        if (left == 1 || right == 1) return 2;

        return 0;
    }
    int minCameraCover(shared_ptr<TreeNode> root) {
        if (traversal(root) == 0) result++;
        return result;
    }
};

TEST(Test968, SimpleTest) {
    auto root = make_shared<TreeNode>(0);
    auto middle = make_shared<TreeNode>(0);
    auto left = make_shared<TreeNode>(0);
    auto right = make_shared<TreeNode>(0);
    root->left = middle; 
    middle->left = left; 
    middle->right = right;
    Solution s; 
    EXPECT_EQ(s.minCameraCover(root), 1);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
