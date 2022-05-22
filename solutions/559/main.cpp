#include <memory> 
#include <queue> 
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

template<typename T>
class Node {
public: 
    T val; 
    vector<shared_ptr<Node<T>>> children; 

    Node() {}
    Node(T _val) : val(_val) {}
    Node(T _val, vector<shared_ptr<Node<T>>> _children) : val(_val), children(_children) {}
};

template<typename T> 
class RecursiveSolution {
public:
    int helper(shared_ptr<Node<T>> node) {
        if (node == nullptr) return 0; 
        int max_depth = 0; 
        for (const auto& child : node->children) {
            max_depth = max(helper(child), max_depth); 
        }
        max_depth++; 
        return max_depth; 
    }
    int maxDepth(shared_ptr<Node<T>> root) {
        return helper(root); 
    }
};

template<typename T> 
class IterativeSolution {
public:
    int maxDepth(shared_ptr<Node<T>> root) {
        if (root == nullptr) return 0; 
        queue<shared_ptr<Node<T>>> mq; 
        mq.push(root); 
        int depth = 0; 
        while (!mq.empty()) {
            const int size = mq.size();
            for (int i = 0; i < size; ++i) {
                shared_ptr<Node<T>> node = mq.front();
                mq.pop(); 
                for (const auto& c : node->children) {
                    mq.push(c); 
                }
            }
            depth++; 
        }
        return depth; 
    }
};

TEST(Test559, SimpleTest) {
    auto root = make_shared<Node<int>>(1);

    auto l11 = make_shared<Node<int>>(3);
    auto l12 = make_shared<Node<int>>(2);
    auto l13 = make_shared<Node<int>>(4);
    root->children.push_back(l11); 
    root->children.push_back(l12); 
    root->children.push_back(l13); 

    auto l21 = make_shared<Node<int>>(5);
    auto l22 = make_shared<Node<int>>(6);
    l11->children.push_back(l21);
    l11->children.push_back(l22);

    RecursiveSolution<int> rs; 
    EXPECT_EQ(rs.maxDepth(root), 3); 
    IterativeSolution<int> is; 
    EXPECT_EQ(is.maxDepth(root), 3); 
}

int main() {
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS(); 
}

