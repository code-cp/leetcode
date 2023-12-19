use std::rc::Rc; 
use std::cell::RefCell; 

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

// use std::rc::Rc;
// use std::cell::RefCell;

// fn main() {
//     let data = Rc::new(RefCell::new(42));

//     // Cloning an Rc increments the reference count
//     let reference1 = Rc::clone(&data);
//     let reference2 = Rc::clone(&data);

//     // Borrowing mutably through RefCell
//     let mut mutable_reference = data.borrow_mut();
//     *mutable_reference += 1;

//     // Since RefCell allows interior mutability, even though data is Rc,
//     // the value can be mutated through the mutable reference
// }

impl Solution {
    pub fn pseudo_palindromic_paths(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(node: Option<&Rc<RefCell<TreeNode>>>, mut mask: i32) -> i32 {
            let check_mask = |mask| return if (mask & (mask - 1)) == 0 { 1 } else { 0 }; 
            if let Some(node) = node {
                let node = node.borrow(); 
                mask ^= 1 << node.val; 
                if node.left.is_none() && node.right.is_none() {
                    return check_mask(mask);
                }
                return dfs(node.left.as_ref(), mask) + dfs(node.right.as_ref(), mask);
            }
            0
        }
        dfs(root.as_ref(), 0)
    }
}