#include <memory> 
#include <queue> 
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
class RecursionSolution {
public:
    bool helper(shared_ptr<TreeNode<T>> left, shared_ptr<TreeNode<T>> right) {
        // base case 
        if (left == nullptr && right != nullptr) return false; 
        else if (left != nullptr && right == nullptr) return false; 
        else if (left == nullptr && right == nullptr) return true; 
        else if (left->val != right->val) return false;
        // recursion 
        // post order traversal, left, right, visit  
        auto inner = helper(left->right, right->left);
        auto outer = helper(left->left, right->right); 
        return inner && outer; 
    }
    bool isSymmetric(shared_ptr<TreeNode<T>> root) {
        if (root == nullptr) return true; 
        return helper(root->left, root->right); 
    }
};

template <typename T> 
class IterativeQueueSolution {
public:
    bool isSymmetric(shared_ptr<TreeNode<T>> root) {
        if (root == nullptr) return true; 
        // can also use stack or vector 
        queue<shared_ptr<TreeNode<T>>> mq; 
        mq.push(root->left); 
        mq.push(root->right); 
        while (!mq.empty()) {
            const int qs = mq.size(); 
            for (int i = 0; i < qs / 2; ++i) {
                shared_ptr<TreeNode<T>> left = mq.front(); 
                mq.pop();
                shared_ptr<TreeNode<T>> right = mq.front(); 
                mq.pop(); 
                if (left == nullptr && right != nullptr) return false; 
                else if (left != nullptr && right == nullptr) return false; 
                else if (left == nullptr && right == nullptr) continue; 
                else if (left->val != right->val) return false; 
                mq.push(left->left); 
                mq.push(right->right); 
                mq.push(left->right); 
                mq.push(right->left); 
            }
        }
        return true; 
    }
};

TEST(Test101, SimpleTest) {
    auto root = make_shared<TreeNode<int>>(1);
    auto left = make_shared<TreeNode<int>>(2);
    auto right = make_shared<TreeNode<int>>(2); 
    root->left = left; 
    root->right = right; 

    RecursionSolution<int> sr; 
    EXPECT_TRUE(sr.isSymmetric(root));
    IterativeQueueSolution<int> iqs; 
    EXPECT_TRUE(iqs.isSymmetric(root));
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS(); 
}