/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sat Oct 30 09:30:22 2021
> Description:   
 ************************************************************************/
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
class RecursiveSolution {
public:
    vector<T> _nums;
    shared_ptr<TreeNode<T>> traversal(T low, T high) {
        if (low > high) return nullptr;
        T middle = low + (high - low) / 2;
        shared_ptr<TreeNode<T>> root = make_shared<TreeNode<T>>(_nums[middle]);
        // note, here is middle-1, not middle, since we already deal with middle
        root->left = traversal(low, middle-1);
        root->right = traversal(middle+1, high);
        return root;
    }
    shared_ptr<TreeNode<T>> sortedArrayToBST(vector<T>& nums) {
        _nums = nums;
        // note, here is _nums.size()-1, not _nums.size()
        return traversal(0, _nums.size()-1);
    }
};

TEST(Test108, SimpleTest) {
    vector<int> nums{
        1, 3
    };
    RecursiveSolution<int> rs; 
    auto root1 = rs.sortedArrayToBST(nums);
    EXPECT_EQ(root1->right->val, 3);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
