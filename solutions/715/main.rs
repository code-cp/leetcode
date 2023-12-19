// use std::cell::RefCell;
// use std::rc::Rc;

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
    root: Option<Box<SegmentTreeNode>>, 
}

impl SegmentTree {
    fn new() -> Self {
        SegmentTree {
            root: Some(
                Box::new(
                    SegmentTreeNode::new(
                    0, 
                    i32::pow(10, 9),  
                    false, 
            ))), 
        }
    }

    // NOTE, use static method to avoid self.update, 
    // since self.update(&mut root) will double borrow 
    fn update(root: &mut Option<Box<SegmentTreeNode>>, i: i32, j: i32, tracked: bool) {
        let root = root.as_mut().unwrap(); 
        
        // check if the input range fully contains the root range 
        if root.lo == i && root.hi == j {
            root.tracked = tracked;
            root.left = None; 
            root.right = None; 
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
            Self::update(&mut root.left, i, j, tracked); 
        } else if i > mid {
            Self::update(&mut root.right, i, j, tracked); 
        } else {
            Self::update(&mut root.left, i, mid, tracked); 
            Self::update(&mut root.right, mid+1, j, tracked); 
        }
    
        root.tracked = root.left.as_ref().unwrap().tracked && root.right.as_ref().unwrap().tracked; 
    }    

    fn add_range(&mut self, i: i32, j: i32) {
        Self::update(&mut self.root, i, j, true); 
    }

    fn query_range(&self, i: i32, j: i32) -> bool {
        self.query(self.root.as_ref().unwrap(), i, j)
    }

    fn remove_range(&mut self, i: i32, j: i32) {
        Self::update(&mut self.root, i, j, false); 
    }

    fn query(&self, root: &SegmentTreeNode, i: i32, j: i32) -> bool {
        if root.lo == i && root.hi == j {
            return root.tracked;
        }

        if root.left.is_none() {
            return root.tracked; 
        }
        let mid = root.lo + (root.hi - root.lo) / 2; 
        if j <= mid {
            return self.query(root.left.as_ref().unwrap(), i, j);
        } else if i > mid {
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