Struct Solution;

// Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
  pub val: i32,
  pub left: Option<Rc<RefCell<TreeNode>>>,
  pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
  #[inline]
  pub fn new(val: i32) -> Self {
    TreeNode {
      val,
      left: None,
      right: None
    }
  }
}

use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn rob(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut dp = vec![vec![0; 2]; 10000];
        let mut ans = 0; 

        fn traverse(root: Option<Rc<RefCell<TreeNode>>>) -> (i32, i32) {
            let mut result = (0, 0); 

            if root.is_none() {
                return result; 
            }

            let root = root.unwrap(); 

            let left = traverse(root.borrow().left.clone()); 
            let right = traverse(root.borrow().right.clone()); 

            // do not steal from cur node 
            result.0 = left.0.max(left.1) + right.0.max(right.1);
            // steal from cur 
            result.1 = root.borrow().val + left.0 + right.0;

            return result;  
        }
        
        let result = traverse(root);

        result.0.max(result.1) 
    }
}