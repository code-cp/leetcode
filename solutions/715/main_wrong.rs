use std::cell::RefCell;
use std::rc::Rc;

struct SegmentTreeNode {
    lo: i32, 
    hi: i32, 
    tracked: bool, 
    left: Option<Box<SegmentTreeNode>>,
    right: Option<Box<SegmentTreeNode>>, 
}

impl SegmentTreeNode {
    fn new(lo: i32, hi: i32, tracked: bool) -> Self {
        SegmentTreeNode {
            lo, 
            hi,
            tracked, 
            left: None, 
            right: None, 
        }
    }
}

struct SegmentTree {
    root: Rc<RefCell<Option<Box<SegmentTreeNode>>>>, 
}

impl SegmentTree {
    fn new() -> Self {
        SegmentTree {
            root: Rc::new(RefCell::new(Some(Box::new(SegmentTreeNode::new(
                0, 
                1e9 as i32, 
                false, 
            )))))
        }
    }

    fn add_range(&mut self, i: i32, j: i32) {
        let mut root = self.root.borrow_mut(); 
        self.update(root.as_mut().unwrap(), i, j, true); 
    }

    fn query_range(&self, i: i32, j: i32) -> bool {
        let root = self.root.borrow(); 
        self.query(root.as_ref().unwrap(), i, j)
    }

    fn remove_range(&mut self, i: i32, j: i32) {
        let mut root = self.root.borrow_mut(); 
        self.update(root.as_mut().unwrap(), i, j, false); 
    }

    fn update(&mut self, root: &mut SegmentTreeNode, i: i32, j: i32, tracked: bool) {
        // check if the input range fully contains the root range 
        if root.lo >= i && root.hi <= j {
            root.tracked = tracked;
            return; 
        }

        let mid = root.lo + (root.hi - root.lo) / 2; 

        if root.left.is_none() {
            root.left = Some(Box::new(SegmentTreeNode::new(
                root.lo, 
                mid, 
                root.tracked, 
            ))); 

            root.right = Some(Box::new(
                SegmentTreeNode::new(mid + 1, root.hi, root.tracked)
            )); 
        }

        if j <= mid {
            self.update(root.left.as_mut().unwrap(), i, j, tracked); 
        } else if i > mid {
            self.update(root.right.as_mut().unwrap(), i, j, tracked); 
        } else {
            self.update(root.left.as_mut().unwrap(), i, mid, tracked); 
            self.update(root.right.as_mut().unwrap(), mid+1, j, tracked); 
        }
        
        // bug is here 
        root.tracked = root.left.as_ref().unwrap().tracked || root.right.as_ref().unwrap().tracked; 
    }

    fn query(&self, root: &SegmentTreeNode, i: i32, j: i32) -> bool {
        if root.lo <= i && root.hi >= j {
            return root.tracked;
        }

        if root.left.is_none() {
            return root.tracked; 
        }
        let mid = root.lo + (root.hi - root.lo) / 2; 
        if j <= mid {
            return self.query(root.left.as_ref().unwrap(), i, j);
        } else if i < mid {
            return self.query(root.right.as_ref().unwrap(), i, j);  
        } else {
            self.query(root.left.as_ref().unwrap(), i, mid) && 
            self.query(root.right.as_ref().unwrap(), mid+1, j)
        }
    }
}

struct RangeModule {
    tree: SegmentTree, 
}

impl RangeModule {
    fn new() -> Self {
        RangeModule {
            tree: SegmentTree::new(), 
        }
    }

    fn add_range(&mut self, left: i32, right: i32) {
        self.tree.add_range(left, right-1); 
    }

    fn query_range(&self, left: i32, right: i32) -> bool {
        self.tree.query_range(left, right-1) 
    }

    fn remove_range(&mut self, left: i32, right: i32) {
        self.tree.remove_range(left, right-1); 
    }
}

// fn main() {
//     let mut obj = RangeModule::new(); 
//     obj.add_range(10, 20); 
//     let res = obj.query_range(14, 16); 
//     assert!(res); 
// }