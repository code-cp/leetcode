#include <queue> 
#include <memory> 
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

template<typename T> 
struct TreeNode {
    T val; 
    shared_ptr<TreeNode<T>> left; 
    shared_ptr<TreeNode<T>> right; 
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(T x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(T x, shared_ptr<TreeNode<T>> left, shared_ptr<TreeNode<T>> right) : 
        val(x), left(left), right(right) {}
};

template<typename T> 
class Solution {
public:
    vector<vector<T>> levelOrder(shared_ptr<TreeNode<T>> root) {
        vector<vector<T>> result; 
        if (root == nullptr) return result; 
        queue<shared_ptr<TreeNode<T>>> mq; 
        mq.push(root); 
        while (!mq.empty()) {
            const int size = mq.size(); 
            vector<T> mv; 
            for (int i = 0; i < size; ++i) {
                shared_ptr<TreeNode<T>> node = mq.front();
                mq.pop();
                mv.push_back(node->val); 
                if (node->left != nullptr) mq.push(node->left); 
                if (node->right != nullptr) mq.push(node->right); 
            }
            result.push_back(mv);
        }
        return result; 
    }
};

TEST(Test102, SimpleTest) {
    auto root = make_shared<TreeNode<int>>(3);
    auto left1 = make_shared<TreeNode<int>>(9);
    auto right1 = make_shared<TreeNode<int>>(20);
    auto left2 = make_shared<TreeNode<int>>(15);
    auto right2 = make_shared<TreeNode<int>>(7);
    root->left = left1; 
    root->right = right1; 
    right1->left = left2; 
    right1->right = right2; 
    Solution<int> s; 
    vector<vector<int>> result = s.levelOrder(root); 
    EXPECT_EQ(result[0][0], 3);
    EXPECT_EQ(result[1][0], 9);
    EXPECT_EQ(result[1][1], 20);
    EXPECT_EQ(result[2][0], 15);
    EXPECT_EQ(result[2][1], 7);
}

int main() {
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS(); 
}