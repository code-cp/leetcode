#include <memory> 
#include <queue> 
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
class PostOrderRecursiveSolution {
public:
    int helper(shared_ptr<TreeNode<T>> node) {
        if (node == nullptr) return 0; 
        // left, right, visit 
        // post order traversal 
        int leftDepth = helper(node->left); 
        int rightDepth = helper(node->right); 
        return max(leftDepth, rightDepth) + 1; 
    }
    int maxDepth(shared_ptr<TreeNode<T>> root) {
        return helper(root); 
    }
};

template<typename T> 
class LevelOrderIterativeSolution {
public:
    int maxDepth(shared_ptr<TreeNode<T>> root) {
        if (root == nullptr) return 0; 
        queue<shared_ptr<TreeNode<T>>> mq; 
        mq.push(root); 
        int result = 0; 
        while (!mq.empty()) {
            const int size = mq.size(); 
            for (int i = 0; i < size; ++i) {
                shared_ptr<TreeNode<T>> node = mq.front();
                mq.pop(); 
                if (node->left != nullptr) mq.push(node->left); 
                if (node->right != nullptr) mq.push(node->right);
            } 
            result++;
        }
        return result; 
    }
};

TEST(Test104, SimpleTest) {
    auto root = make_shared<TreeNode<int>>(1); 
    auto right = make_shared<TreeNode<int>>(2);
    root->right = right; 
    PostOrderRecursiveSolution<int> prs; 
    const int depth1 = prs.maxDepth(root); 
    LevelOrderIterativeSolution<int> lis; 
    const int depth2 = lis.maxDepth(root); 
    EXPECT_EQ(depth1, 2); 
    EXPECT_EQ(depth2, 2); 
}

int main() {
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS(); 
}